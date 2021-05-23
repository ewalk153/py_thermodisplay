# Micropython Temperature Display

Fetching data from a web server and displays it on a ST7789 color screen.

Written in python. Access to web server is protected with a shared secret.

## Setup

1. Copy example_settings.py to settings.py
2. Install ampy to easily deploy files to the Micropython embedded device. Configure ~/.ampy with your device location

## Deployment
1. Deploy the app by copying the .py files from this project to the device:
```
for f in *.py; do ampy put $f; done
```
