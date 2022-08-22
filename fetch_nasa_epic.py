"""\
Take number of NASA EPIC (Earth PolychromatIc Camera) and
saving them in "./images"
"""

import os.path
import requests
import argparse
from dotenv import load_dotenv

from utils.image_operations import load_image


def create_parser():
    parser = argparse.ArgumentParser(
        description='Take number of NASA EPIC (Earth PolychromatIc Camera) and'
                    'saving them in "./images"'
    )
    parser.add_argument(
        '-ic',
        '--image_count',
        default=1,
        help='Number of EPIC images to be downloaded and saved.'
    )
    return parser


def assemble_nasa_epic_url(image_info, color_mode):
    """Assembling info for EPIC image url"""

    image_extension = 'png'
    date = (image_info["date"].split()[0]).replace('-', '/')
    image_name = f'{image_info["image"]}.{image_extension}'
    image_url = f'https://epic.gsfc.nasa.gov/archive/{color_mode}/{date}/' \
                f'{image_extension}/{image_name}'
    return image_url


def fetch_nasa_epic(image_count=1):
    """Download image_count number of images from EPIC and save to arg path"""

    path_for_saved_image = './images'
    nasa_token = os.getenv('API_TOKEN_NASA')

    # Getting info for EPIC image url
    color_mode = 'enhanced'    # 'natural' or 'enhanced'
    params = {
        'api_key': nasa_token,
    }
    url = f'https://api.nasa.gov/EPIC/api/{color_mode}/'

    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_info_list = response.json()
    for count, image_info in enumerate(epic_info_list):
        if count == image_count:
            break
        epic_url = assemble_nasa_epic_url(image_info, color_mode)
        load_image(epic_url, path_for_saved_image, f'epic_image_{count}')


def main():
    load_dotenv()
    parser = create_parser()
    args = parser.parse_args()
    image_count = args.image_count
    try:
        fetch_nasa_epic(image_count)
        print(f'{image_count} image(s) was/were successfully downloaded.')
    except requests.exceptions.HTTPError:
        print("Can't download images from EPIC.")


if __name__ == '__main__':
    main()
