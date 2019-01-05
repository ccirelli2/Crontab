#!/usr/bin/env python
import datetime



Now = datetime.datetime.now()



myFile = open('/tmp/append.txt', 'a')
myFile.write('hello world, the time is {}'.format(Now))

