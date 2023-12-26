import os
import time
import requests
from datetime import datetime, timedelta

   os.system("clear")
    print(logo)
    name = input(" WHAT IS YOUR FIRST NAME? : ")
    first_name = name.split()[0]
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/YUJI052000/Tool/blob/main/Approval.txt").text
    if id in DARK:
        YUJI()
    else:
        os.system("clear")
        time.sleep(2.0)
        
        os.system("clear")
        print(logo)
        print(" \33[1;32m PLEASE GET APPROVAL FIRST\33[1;37m ")
        time.sleep(1)
        os.system('clear')
        print(logo)
        print("")
        print(" \33[1;32m YUJI GREIGOR [Black Market] \33[1;37m ")
        print(" \33[1;32m Note : THIS IS A PAID TOOL!   \33[1;37m")
        print ("")
        print(" Mode of Payment : GCASH ")
        print("")
        print(" Your key is not Approved. ")
        print("")
        print(" Copy and Send Key To Yuji Greigor")
        print ("")
        print(" Your Key : " + first_name + "-" + id)
        print ("")

        time_limit = 1 # hours
        key_approval_date = datetime.now()
        key_expiration_date = key_approval_date + timedelta(hours=time_limit)

        print(f" Key Expiration Date: {key_expiration_date}")
        print(f" Your key will be removed from approval.txt after {time_limit} hours")
        input(" Press Enter To Send Key")

        time.sleep(time_limit * 3600)
        with open("Approval.txt", "r") as file:
            lines = file.readlines()
        with open("Approval.txt", "w") as file:
            for line in lines:
                if line.strip() != id:
                    file.write(line)
