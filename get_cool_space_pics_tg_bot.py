'''Creating bot that send space pics to space pics channel'''

import os.path
import random
from dotenv import load_dotenv
import telegram


def get_random_picture_name(path_to_pictures):
    pictures = os.listdir(path_to_pictures)
    return random.choice(pictures)


def send_photo(bot):
    path_to_pictures = './images'
    picture_name = get_random_picture_name(path_to_pictures)
    bot.send_photo(
        chat_id='@coolspacepics',
        photo=open(f'{path_to_pictures}/{picture_name}', 'rb')
    )


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    bot = telegram.Bot(token=tg_bot_token)
    send_photo(bot)


if __name__ == '__main__':
    main()
