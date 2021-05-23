# Micropython Temperature Display

Fetching data from a web server and displays it on a ST7789 color screen.

Written in python. Access to web server is protected with a shared secret.

## Setup

1. Copy example_settings.py to settings.py
2. Install [ampy](https://github.com/scientifichackers/ampy) to easily deploy files to the Micropython embedded device. Configure ~/.ampy with your device location

## Deployment
1. Deploy the app by copying the .py files from this project to the device:
```
make deploy
```

## Running a script locally
Changes can be tested without running the whole deploy process. Simply run;

```
make run
```

or
```
ampy run main.py
```
