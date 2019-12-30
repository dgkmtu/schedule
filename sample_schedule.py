# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:25:58 2019

@author: yinag
"""

import schedule
import time

def job():
    print("job実行")


#1分毎にjobを実行
schedule.every(1).minutes.do(job)

#1時間毎にjobを実行
schedule.every(1).hours.do(job)

#AM11:00にjobを実行
schedule.every().day.at("11:00").do(job)

#日曜日にjobを実行
schedule.every().sunday.do(job)

#水曜日の13:15にjobを実行
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



    
