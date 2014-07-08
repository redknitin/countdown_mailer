__author__ = 'nitinr'

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('settings.ini')

from datetime import datetime


def num_days():
    global cfg
    evtname = cfg['Event']['EventName']
    evtdate = cfg['Event']['TargetDate']
    evtdate = datetime.strptime(evtdate, '%d-%m-%Y')
    todaydate = datetime.today()
    delta_days = evtdate - todaydate
    num_days = delta_days.days + (1 if delta_days.seconds > 0 else 0)
    return num_days