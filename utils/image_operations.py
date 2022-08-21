import os.path
from urllib.parse import urlsplit, unquote

import shutil
from pathlib import Path
import requests


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


def clear_images_folder():
    shutil.rmtree('../images', ignore_errors=True)
