#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='michielcastelein')
cron.remove_all()

#add new cron job
job  = cron.new(command='my_path.py')

#job settings
job.minute.every(3)
cron.write()
