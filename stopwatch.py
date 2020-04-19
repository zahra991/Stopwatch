# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:28:54 2020

@author: ZAHRA
"""

import time
def time_convert(sec):
   mins= sec // 60
   sec = sec % 60
   hours = mins //60
   mins = mins %6
   print("Time lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
   
input("Press Enter to start the Stopwatch")
start_time=time.time() #to get the current time
try:
    hours=0
    while True:
        for minutes in range(0,60):
            for seconds in range(0,60):
                time.sleep(1)
                print(hours,":",minutes,":",seconds+1)
except KeyboardInterrupt: # ctrl+C to interrupt the execution
    end_time=time.time()
    time_lapsed = end_time-start_time
    time_convert(time_lapsed)
    
    