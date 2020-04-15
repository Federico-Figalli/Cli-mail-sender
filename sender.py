#!/usr/bin/python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
import configparser
import argparse
import smtplib
import logging
import sys

sender_config = configparser.ConfigParser()
config_file = 'sender.conf'

def start():
    echo_bash = ''.join(sys.stdin.readlines())
    mail_To_Sender = mail_To.split(",")
    sender_config.read(config_file)
    msg = MIMEMultipart()
    server_mail = sender_config['server']['stmp']
    server_port = sender_config['server']['port']

    user = sender_config['user']['user']
    password = sender_config['password']['psw']

    msg['From'] = sender_config['message']['from']
    msg['Subject'] = mail_subj
    reply = sender_config['message']['reply']
    msg.add_header('reply-to', reply)

    try:
        # create server
        server = smtplib.SMTP(server_mail, server_port)
        server.starttls()
        # Login Credentials for sending the mail
        server.login(user, password)
        # send the message via the server.
        message = echo_bash
        msg.attach(MIMEText(message, 'plain'))
        print(mail_To_Sender)
        server.sendmail(msg['From'], mail_To_Sender, msg.as_string())
        print('Subject is %s' % msg['Subject'])

        server.quit()

    except:
        print(' Problem on smtp server')

print('\n Sender mail. Type -h for read insert option \n')
parser = argparse.ArgumentParser(description='Sender mail')
parser.add_argument('-r', action='store',
                    dest='reply_To_Address', help='Mail address to respond')
parser.add_argument('-s', action='store', dest='subj',
                    help='Add subject at mail')
parser.add_argument('-d', action='store', dest='mail',
                    help='Add one or more destinations mail address')
parser.add_argument('-V', action='version',
                    version='The version of %(prog)s 0.1')
parser.add_argument('-c', action='store_const',
                    const=' The path are in: %s' % config_file, dest='p', help='See the PATH of sender.conf file')
arg = parser.parse_args()

results = parser.parse_args()
mail_To = results.mail
mail_subj = results.subj
reply = results.reply_To_Address

if ((path.exists(config_file) is False) or (mail_To is None)):
    if (path.exists(config_file) == False):
        print('\n File %s not exist in the path directory \n' % config_file)
        exit()
    else:
        print('\n Required params not insert. Used -h for read istruction \n')
        exit()

start()
