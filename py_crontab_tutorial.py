# DOCUMENTATION:
'''
Source:     https://stackabuse.com/scheduling-jobs-with-python-crontab/


'''


# Import Library
from crontab import CronTab

# Access Class Object
cron = CronTab()


# Create Function
script = 'test_crontab.py'

# Create A New Job
job = cron.new(command = script)
job.minute.every(1)
job.enable()
