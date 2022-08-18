import os.path
from urllib.parse import urlsplit, unquote

import shutil
from pathlib import Path
import requests
from dotenv import load_dotenv


def get_file_extension_from_url(url):
    '''Get URL with image and return extension'''

    url_attributes = urlsplit(url)
    image_path = unquote(url_attributes.path)
    image_fullname = os.path.split(image_path)[1]
    return os.path.splitext(image_fullname)[1]


def load_image(image_url, path_to_save, image_name):
    '''Get URL image_url and save to path_to_save path'''

    Path(path_to_save).mkdir(exist_ok=True)
    response = requests.get(image_url)
    response.raise_for_status()
    image_extension = get_file_extension_from_url(image_url)
    with open(f'{path_to_save}/{image_name}{image_extension}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(path_for_saved_image='./images'):
    '''Fetching images from last or certain SpaceX launch and saving them'''

    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()
    images_urls = images["links"]["flickr"]["original"]

    for count, image in enumerate(images_urls):
        load_image(
            image,
            path_for_saved_image,
            f'spacex_{count}'
        )


def fetch_nasa_apod(path_for_saved_image='./images', image_count=20):
    '''Download 30 pictures of a day and saving them in path by arg'''

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


def assemble_nasa_epic_url(image_info, color_mode):
    '''Assembling info for EPIC image url'''

    image_extension = 'png'
    date = (image_info["date"].split()[0]).replace('-', '/')
    image_name = f'{image_info["image"]}.{image_extension}'
    image_url = f'https://epic.gsfc.nasa.gov/archive/{color_mode}/{date}/' \
                f'{image_extension}/{image_name}'
    return image_url


def fetch_nasa_epic(path_for_saved_image='./images', image_count=5):
    '''Download one image from EPIC and save to arg path'''

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
    shutil.rmtree('./images', ignore_errors=True)
    path_for_saved_image = './images'

    try:
        fetch_spacex_last_launch(path_for_saved_image)
        fetch_nasa_apod(path_for_saved_image, 5)
        fetch_nasa_epic(path_for_saved_image, 5)
    except requests.exceptions.HTTPError:
        print('Catch HTTPError')


if __name__ == '__main__':
    main()
