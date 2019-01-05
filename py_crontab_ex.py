from crontab import CronTab

cron = CronTab(user='ccirelli2')
job = cron.new(command='python example1.py')
job.minute.every(1)

cron.write()


