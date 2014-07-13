__author__ = 'nitinr'

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('settings.ini')

from datetime import datetime

import logging
logging.basicConfig(level=10, filename='mailer.log', format='%(asctime)s - %(levelname)s - %(message)s')


def num_days():
    """
    Calculates the number of days remaining, rounded up
    (i.e. if there are 3 hours remaining for tomorrow, the function returns 1 day remaining for tomorrow)
    :return:
    """
    global cfg
    evtname = cfg['Event']['EventName']
    evtdate = cfg['Event']['TargetDate']
    evtdate = datetime.strptime(evtdate, '%d-%m-%Y')
    todaydate = datetime.today()
    delta_days = evtdate - todaydate
    num_days = delta_days.days + (1 if delta_days.seconds > 0 else 0)
    return num_days