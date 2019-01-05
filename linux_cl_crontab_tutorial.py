'''DOCUMENTATION


Source Information-----------------------------------------
Video:  How to use crontab commadn (youtube)
Syntax:     https://crontab.guru/#0_8_*_*_1-5


Commands -------------------------------------------------
crontab -l     List jobs
crontab -e     add job
crontab -r     remove job

syntax:     *****   every timer has 5 values.  
            *       *       *           *       *
            minute  hour    day         month   day 
                            (of month)          (of week)
1 - minute (0-59)
2 = hour (24hrs 0-23)
3 = day of month (1-31)
4 = month of year (1-12)
5 = day of week (0-6)

comma:      used to specify two values.  0 0 1,15 * *   that 1,15 means that it will run on the 1st and 
                                                        15th of every month. Must specify time, here 0 0
                                                        means that it will run at 0 min of 0 hour of 
                                                        the 1st and 15th of every month. 
Defining Intervals      forward slash
        ex:             */10 * * * *    This will run every 10 minutes of every day of every month 


Examples Syntax:
    every minute        * * * * * 
    at 6:01 12/20/18    1 6 * * * 
    at 8:00 on every 
    day of the week
    from M-F            0 8 * * 1-5



# Create Crontab File
crontab -e


or

vim file_name.cron              # Creates a cron file

crontab file_name.cron          # Load file into crontab

crontab -e                      # Check that it is there







'''






