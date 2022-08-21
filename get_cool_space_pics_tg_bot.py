from dotenv import load_dotenv
import os.path
import telegram


def main():
    load_dotenv()
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    bot = telegram.Bot(token=tg_bot_token)
    print(bot.get_me())
    bot.send_message(
        chat_id='@coolspacepics',
        text='Space is cool!'
    )

if __name__ == '__main__':
    main()