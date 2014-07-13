#
# -=[ Countdown Mailer ]=-
# (Gotcha: This app is hard-coded to use GMail's SMTP; Supports only 1 event)
# Description: Sends the countdown to an event by email
# Instructions: Make updates to settings.ini and schedule mailer.py to run daily
#

__author__ = 'Nitin Reddy Katkam'

import smtplib
from email.mime.text import MIMEText
import configparser

cfg = configparser.ConfigParser()
cfg.read('settings.ini')

import logging
logging.basicConfig(level=10, filename='mailer.log', format='%(asctime)s - %(levelname)s - %(message)s')


def send_email(content):
    """
    Connects to the SMTP server and sends out the email message
    :return:
    """
    global cfg

    from_email = cfg['Mail']['FromEmail']
    from_pass = cfg['Mail']['FromPass']
    to_email = cfg['Mail']['ToEmail']
    subject = cfg['Mail']['Subject']
    logging.debug('Email from %s to %s with subject %s' % (from_email, to_email, subject))

    logging.debug('Connecting to SMTP server')
    srv = smtplib.SMTP('smtp.gmail.com', 587)
    srv.ehlo()
    srv.starttls()
    srv.ehlo()
    srv.login(from_email, from_pass)

    to_addrs = to_email.split(';')
    for iter_to in to_addrs:
        iter_to = iter_to.strip()
        if iter_to == '':
            continue
        try:
            msg = MIMEText(content)
            msg['Subject'] = subject
            srv.sendmail(from_email, iter_to, msg.as_string())
            logging.debug('Email sent to %s' % iter_to)
        except Exception as xcpt:
            logging.error(str(xcpt))

    srv.quit()
    srv.close()
    logging.debug('Disconnecting from server')