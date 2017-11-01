# -*- coging:utf-8 -*-
# smple_code


from __future__ import print_function
import io
import socket
import time
import picamera
import RPi.GPIO as GPIO
import datetime
import smtplib
from contextlib import closing
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.Header import Header
from email.Utils import formatdate
from smtplib import SMTP_SSL

def main():
  camera = picamera.PiCamera()
  camera.brightness = 70
  camera.hflip = True
  camera.vflip = True
  camera.resolution = (1024, 768)
  cnt = 0
  COMMASPACE = ', '
  add = ['LIST1@MAILADDRESS, LIST2@MAILADDRESS']
  me = 'ME@MAILADDRESS'
  smtp_server = 'smtp.gmail.com'
  port = 465
  passwd = 'PASSWORD'

  while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    inputValue1 = GPIO.input(4)

    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(18, GPIO.IN)
    # inputValue2 = GPIO.input(18)

    inputValue2 = False

    stream = io.BytesIO()

    if (inputValue1 == True or inputValue2 == True):

      # pic 1
      file = 'smp01/smp'+ str(datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")) +'.jpeg'
      print(file)

      camera.start_preview()
      camera.capture(file)

      fp = open(file, 'rb')
      img = fp.read()
      mj = MIMEImage(img, 'jpeg', filename=file)
      fp.close()

      # pic 2
      file = 'smp01/smp'+ str(datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")) +'.jpeg'
      print(file)

      camera.start_preview()
      camera.capture(file)

      fp = open(file, 'rb')
      img = fp.read()
      mj = MIMEImage(img, 'jpeg', filename=file)
      msg = MIMEMultipart()
      msg['Subject'] = ("Test : Bear apperarance information")
      msg['To'] = COMMASPACE.join(add)
      msg.premble = 'Test mail'
      msg.attach(mj)
      fp.close()


      # Send e-mail
      s = SMTP_SSL(smtp_server, port)
      s.login(me, passwd)
      s.sendmail(me, add, msg.as_string())
      s.close()
      print('email send')

    else:
      print (str(cnt).zfill(4) + ' : '+ str(inputValue1) + ',' +str(inputValue2))
    time.sleep(1)
    cnt+=1

if __name__ == '__main__':
  main()



