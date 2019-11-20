#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import sys
import string
import re

reload(sys)
sys.setdefaultencoding('UTF8')
app = Flask(__name__)
client = Client('ACb89307719aa8043871f9912452ef21c6', \
                '2f56bc2c9d8ae27afa3baf74fb46f0cb')

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

me = ""

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    r = request.form['Body']
    message_body = re.sub(r'[^\w\s]','',r.lower())
    resp = MessagingResponse()
    response = "Sorry that is not a valid response. Note: the responses are not" + \
               "case-sensitive and ignore punctuation so you must have really fucked something up."
    if message_body == "pls stahp":
    	response = "I lied. This isn't going to stop the texts." +  \
                    " Please respond with \"get lost loser\" to stop the texts."
    elif message_body == "get lost loser":
        response = "I lied again. These aren't going to stop until you eat food w/ me ;)" + \
                   " If you change your mind please type \"I am ready to schedule a date.\""
    elif message_body == "i am ready to schedule a date":
        response = "Great! Would you like to make a lunch or dinner date? Please type \"lunch\" or \"dinner\""
    elif message_body == "lunch" or message_body == "dinner":
        response = "Okay! What day would you like the date to be on? Please type a day of the week."
    elif message_body in days:
        response = "Awesome! I'll inform Master Steven of the development and he will get back to you in the next 7 business days."
    elif message_body[0:3] == "bug":
        response = "Thanks for the bug report. Master Steven apprectates your feedback."
    elif message_body == "information":
    	response = "Yes this is dumb. Yes I should have been studying for finals instead of making this. Hope you like it :)"
    resp.message(response)
    fwd_msg = "Her response was: " + r
    client.messages.create(from_="+12175763259",to=me,body=fwd_msg)
    return str(resp)
                          
if __name__ == '__main__':
    app.run()
