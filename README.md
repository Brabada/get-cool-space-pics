# Publish Space Pics!

Project that can download cool space pics and publish them to the TG channel.

That's include:

**fetch_nasa_apod.py** — download NASA APOD (**A**stronomy **P**icture **O**f **D**ay) to
`'./images'` folder.

**fetch_nasa_epic.py** — download NASA EPIC (**E**arth **P**olychromat**I**c **C**amera) 
beautiful pictures of Earth to `'./images'` folder.

**fetch_spacex_images.py** — download photos from the latest SpaceX launch or from particular
launch by launch id to `'./images'` folder.

**publish_images_tg_channel.py** — publish random photos from `'./images'` folder to the
Telegram channel by bot.


## How to install
For start, you need `Python 3` and `pip`
Also you should get NASA token API from here: https://api.nasa.gov/

It's look like that: `a18b7a8d412ea74b17bda2a06f1b69fa3805a712`

After you should create `.env` file in the script's folder and add this token:
```shell
$ cd "path_where_is_script" 
$ echo API_TOKEN_NASA=a18b7a8d412ea74b17bda2a06f1b69fa3805a712 > .env
```
Installing all required packages:
```shell
$ cd "path_where_is_script"
$ pip install -r requirements.txt
```

Get Telegram bot token from [@BotFather](https://telegram.me/BotFather) by 
[this manual](https://core.telegram.org/bots#3-how-do-i-create-a-bot), if you 
don't have any. 
After, add Telegram bot token to `.env` file:
```shell
$ echo -e TG_BOT_TOKEN=your_token\n >> .env
```
Create TG channel and add your bot to the channel. Then add `CHAT_ID` with your channel
`@channelname` to `.env` file:
```shell
$ echo -e CHAT_ID=@coolspacepics\n >> .env 
```

## How to launch
Launching script:
```shell
$ cd "path_where_is_script"
$ python publish_images_tg_channel.py -p hours_number
```
`hours_number` is period in hours (float) for posting new image.

Make sure that `./images` folder have images.

## Troubleshooting