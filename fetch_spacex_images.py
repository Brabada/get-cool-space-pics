'''Fetching images from last or certain SpaceX launch id argument and saving
them to ./images folder'''

import requests
import argparse

from utils.image_operations import load_image


def create_parser():
    parser = argparse.ArgumentParser(
        description='Script gets SpaceX launch id as argument and save images '
                    'in ./images folder. If no argument provided returned '
                    'images from last launch'
    )
    parser.add_argument(
        '-fl_id',
        '--flight_id',
        help='Flight id of SpaceX launch. Example: 5eb87d46ffd86e000604b388',
        default='latest'
    )
    return parser


def fetch_spacex_images(flight_url):
    response = requests.get(flight_url)
    response.raise_for_status()
    images = response.json()
    images_urls = images["links"]["flickr"]["original"]
    path_for_saved_image = './images'
    for count, image in enumerate(images_urls):
        load_image(
            image,
            path_for_saved_image,
            f'spacex_{count}'
        )


def main():
    '''Get flight_id and returned images (if they're exist) to ./image
    folder'''

    parser = create_parser()
    args = parser.parse_args()
    flight_id = args.flight_id
    flight_url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    try:
        fetch_spacex_images(flight_url)
        print('Images saved in ./images folder')
    except requests.exceptions.HTTPError:
        print(f"Can't get photos by followed id: {flight_id}")


if __name__ == '__main__':
    main()
