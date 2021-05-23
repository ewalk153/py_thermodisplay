import settings
import sys
import time
import machine
import st7789py as st7789
import uos
import random
import network
import urequests as requests
import ujson as json
import romans
from machine import Pin

bl = machine.Pin(5, machine.Pin.OUT)
bl.value(1)
 
spi = machine.SPI(1, baudrate=80000000, polarity=1, phase=0, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12))#HSPI
 
display = st7789.ST7789(
    spi, 240, 240,
    reset=machine.Pin(21, machine.Pin.OUT),
    dc=machine.Pin(22, machine.Pin.OUT),
    cs=machine.Pin(15, machine.Pin.OUT),
    backlight=machine.Pin(5, machine.Pin.OUT),
)

#Connection Network
wlan=0
def connectWiFi(ssid, passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid, passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
def random_color():
  return st7789.color565(
  random.getrandbits(8),
  random.getrandbits(8),
  random.getrandbits(8))
 
def print_lines(lines, color=st7789.BLUE):
    row = 0
    for line in lines:
        row += 32
        display.text(romans, line, row, 0, color)
def print_temperature():
    url = settings.settings['temp_url']
    headers = { 'secret' : settings.settings['secret'] }
    r = requests.get(url, headers=headers)

    json_body = json.loads(r.content)
    lines = ["Temp: " + str(json_body['temperature']), json_body['local_time']]
    display.fill(st7789.BLACK)
    print_lines(lines, random_color())
    r.close()
    print('run complete')

display.init() #initialize
display.fill(st7789.BLACK)
 
print_lines(["Running"], st7789.BLUE)

connectWiFi(settings.settings['ssid'], settings.settings['password'])
print('wifi connected')
while True:
    print_temperature()
    time.sleep(10*60) # refresh every 10 minutes
