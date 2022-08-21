'''Publish images to channel by bot every N hour'''

import time
import os.path
import random
from dotenv import load_dotenv
import telegram
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Script publish posts from "./images folder with images '
                    'every N hours. Where N - is IN argument.'
    )
    parser.add_argument('-p',
                        '--period',
                        default=4,
                        help='Posting period in hours. Type float (ex: 0.1, '
                             '1, 3.5)',
                        type=float)
    return parser


def send_photo(image_path):
    '''Publish photo from image_path by bot to channel'''

    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    bot = telegram.Bot(token=tg_bot_token)
    chat_id = os.getenv("CHAT_ID")
    bot.send_photo(
        chat_id=chat_id,
        photo=open(image_path, 'rb')
    )


def get_images_paths(path_root):
    '''Parse path_root for images and return list of images paths'''

    images_paths = []
    for address, dirs, files in os.walk(path_root):
        for name in files:
            images_paths.append(os.path.join(address, name))
    return images_paths


def main():
    load_dotenv()
    parser = create_parser()
    args = parser.parse_args()
    period = args.period * 3600

    images_paths = get_images_paths('.\\images')
    while True:
        random.shuffle(images_paths)
        for image_path in images_paths:
            send_photo(image_path)
            time.sleep(period)


if __name__ == '__main__':
    main()
