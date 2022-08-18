# Get Space Pics

Project that download cool space pics from latest SpaceX launches, NASA APOD
(**A**stronomy **P**icture **O**f **D**ay) and NASA EPIC
(**E**arth **P**olychromat**I**c **C**amera) or shortly beautiful pictures of Earth.

## How to install
For start you need `Python 3` and `pip`
Also you should get NASA token API from here: https://api.nasa.gov/

It's look like that: `a18b7a8d412ea74b17bda2a06f1b69fa3805a712`

After you should create `.env` file in the script's folder a    nd add this token:
```shell
$ cd "path_where_is_script" 
$ echo API_TOKEN_NASA=a18b7a8d412ea74b17bda2a06f1b69fa3805a712 > .env
```
Installing all required packages:
```shell
$ cd "path_where_is_script"
$ pip install -r requirements.txt
```

## How to launch
Launching script:
```shell
$ cd "path_where_is_script"
$ python main.py
```
After that you receive brand new pics in `./images` folder.

## Troubleshooting