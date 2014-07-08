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


from countdown import num_days as no_days
num_days = no_days()


def get_content():
    global num_days
    evtname = cfg['Event']['EventName']
    return str(cfg['Mail']['MessageTpl']) % {
        'name': evtname,
        'countdown': num_days
    }


def send_email():
    """
    Main method
    :return:
    """
    global cfg

    from_email = cfg['Mail']['FromEmail']
    from_pass = cfg['Mail']['FromPass']
    to_email = cfg['Mail']['ToEmail']
    subject = cfg['Mail']['Subject']

    srv = smtplib.SMTP('smtp.gmail.com', 587)
    srv.ehlo()
    srv.starttls()
    srv.ehlo()
    srv.login(from_email, from_pass)

    msg = MIMEText(get_content())
    msg['Subject'] = subject
    srv.sendmail(from_email, to_email, msg.as_string())

    srv.quit()
    srv.close()


def main():
    global num_days

    if num_days <= 0:
        print('Event has lapsed')
        return

    send_email()
    print('Done!')


if __name__ == '__main__':
    main()