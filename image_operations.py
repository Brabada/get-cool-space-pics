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
        fetch_nasa_epic(path_for_saved_image, 5)
    except requests.exceptions.HTTPError:
        print('Catch HTTPError')


if __name__ == '__main__':
    main()
