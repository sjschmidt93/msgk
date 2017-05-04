#!/usr/bin/python
# -*- coding: utf-8 -*-
import schedule
import time
from twilio.rest import Client

client = Client('ACb89307719aa8043871f9912452ef21c6','2f56bc2c9d8ae27afa3baf74fb46f0cb')

victim = ""

def job1():
	client.messages.create(from_="+12175763259",to=victim,body="NOON")

def job2():
	client.messages.create(from_="+12175763259",to=victim,body="Midnight")

init_msg =  "You are now subscribed to automated texts to assist" + \
            " you in scheduling a lunch and/or dinner date with Steven." + \
            " You will be reminded twice a day." + \
            " To stop these texts type \"pls stahp.\"" + \
            " To schedule a date please type \"I am ready to schedule a date.\"" + \
            " To report a bug in the software please type \"bug: \" followed by a description of the bug." + \
            " For more information please type \"information.\""

client.messages.create(from_="+12175763259",to=victim,body=init_msg)

schedule.every().day.at("12:00").do(job1)
schedule.every().day.at("00:00").do(job2)

while True:
	schedule.run_pending()
	time.sleep(1)
