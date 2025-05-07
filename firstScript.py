import os
import time

import csv
import datetime

#1) salvestada tulemused failisse  ping_log.csv
# Time,status
# 05.04.2025,OK
# 05.04.2025,Fail
# hosts= ["8.8.8.8","1.1.1.1", "192.168.56.1" ]
#

def checkconection():
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


def taskScaner()
    with open("taskid.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time","Proccess name","Memory Usage"])

    # Running the aforementioned command and saving its output
    output = os.popen("tasklist").read()
    test = output.splitlines()
    for i in range(7,len(test)):
        now = datetime.datetime.now()
        proccesName = test[i].split()
        name = proccesName[0]
        memory = proccesName[-2]
        
        with open("taskid.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now,name,memory])

        print("time: ",now, "name: ", name,"memory: ", memory )
        

if int(input("sisesta number")) == 1:
    checkconection()
else:
    taskScaner()

print("test")
