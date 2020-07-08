import time
import datetime
print ("Current time : " + datetime.datetime.today().strftime("%H") + " : " + datetime.datetime.today().strftime("%M"))
c_hour = int(datetime.datetime.today().strftime("%H"))
c_minute = int(datetime.datetime.today().strftime("%M"))
a_hour=int(input("Enter the Hour: "))
a_minute=int(input("Enter the Minute: "))
while True :
    c_hour = int(datetime.datetime.today().strftime("%H"))
    c_minute = int(datetime.datetime.today().strftime("%M"))
    if ((c_hour == a_hour) and (c_minute == a_minute)) :
        print ("ALARM ... ALARM ... ")
        print ("Current time : " + datetime.datetime.today().strftime("%H") + " : " + datetime.datetime.today().strftime("%M"))
        print ("ALARM ... ALARM ... ")
        break
    time.sleep(1)
    
