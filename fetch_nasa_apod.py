'''\
Script gets number of NASA APOD (Astronomy Picture Of Day) and downloads
 and saving them in ./image folder.'''

import os.path
from dotenv import load_dotenv
import requests
import argparse

from utils.image_operations import load_image


def create_parser():
    parser = argparse.ArgumentParser(
        description='Script gets number of NASA APOD (Astronomy Picture Of '
                    'Day), downloads and saving them in ./image folder.'
    )

    parser.add_argument('-ic',
                        '--image_count',
                        default='1',
                        help='Number of APOD for download.')
    return parser


def fetch_nasa_apod(image_count=1):
    '''Download 30 pictures of a day and saving them in path by arg'''

    path_for_saved_image = './images'
    nasa_token = os.getenv('API_TOKEN_NASA')
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'count': image_count,
        'api_key': nasa_token,
        'thumbs': True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_urls = response.json()
    for count, url in enumerate(response_urls):
        if url['media_type'] == 'video':
            image_url = url["thumbnail_url"]
        else:
            image_url = url["url"]

        load_image(image_url, path_for_saved_image, f'nasa_apod_{count}')


def main():
    load_dotenv()
    parser = create_parser()
    args = parser.parse_args()
    image_count = args.image_count
    try:
        fetch_nasa_apod(image_count)
        print(f'{image_count} image(s) was/were successfully downloaded.')
    except requests.exceptions.HTTPError:
        print("Can't download APOD from server.")


if __name__ == '__main__':
    main()
