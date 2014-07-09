#
# -=[ Countdown Mailer ]=-
# (Gotcha: This app is hard-coded to use GMail's SMTP; Supports only 1 event)
# Description: Sends the countdown to an event by email
# Instructions: Make updates to settings.ini and schedule main.py to run daily
#

__author__ = 'Nitin Reddy Katkam'


import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.ini')

from mailer import send_email

import logging
logging.basicConfig(level=10, filename='mailer.log')

from countdown import num_days as no_days
try:
    num_days = no_days()
except Exception as xcpt:
    logging.error(str(xcpt))


def get_content():
    global num_days
    evtname = cfg['Event']['EventName']
    return str(cfg['Mail']['MessageTpl']) % {
        'name': evtname,
        'countdown': num_days
    }


def main():
    global num_days
    logging.debug('Mailer script invoked.')

    if num_days <= 0:
        print('Event has lapsed')
        logging.warning('The event has lapsed. Num days is %s' % num_days)
        return

    logging.debug('Sending email')
    try:
        send_email(get_content())
    except Exception as xcpt:
        logging.error(str(xcpt))
    print('Done!')


if __name__ == '__main__':
    main()