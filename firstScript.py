import os
import time

import csv
import datetime

#1) salvestada tulemused failisse  ping_log.csv
# Time,status
# 05.04.2025,OK
# 05.04.2025,Fail
hosts= ["8.8.8.8","1.1.1.1", "192.168.56.1" ]

with open("ping_log.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time","Status"])

while True:
    print("kättesadavuse kontroll")
    now = datetime.datetime.now()
    result = ""
    for elem in hosts:
        response = os.system(f"ping -n 1 {elem} > null")
        if response == 0:
            result = "OK"
            print(elem, "kätesadavalt")
        else:
            result = "Fail"
            print(elem, "ei ole kättesadavalt")
        
        with open("ping_log.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now,result])


        print("-"*30)
        time.sleep(5)