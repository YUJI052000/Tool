import random
import time

def main():
    while True:
        sp(0.5)
        print("\n🔰FRESH UA GENERATOR v2.0.0 by Mandean Meddah🔰")
        sp(0.5)
        print("\n1. Generate New UA")
        print("2. Update UA Automatically")
        print("3. Exit")
        sp(0.5)
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_new_ua()
        elif choice == "2":
            update_ua_automatically()
        elif choice == "3":
            exit()
        else:
            print("\nInvalid choice. Please try again.\n")

def generate_new_ua():
    num_uas = int(input("Enter the number of unique User-Agent strings you want to generate: "))

    for i in range(num_uas):
        ua1 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTR;FBDV/Android SDK built for x86;FBMD/x86;FBSN/;FBSV/8.1.0;FBSS/Android 8.1.0;FBCA/armeabi-v7a:x86;]"
        ua2 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBDM/{density=2.0,width=720,height=1472};FBLC/en_PH;FBCR/ASUS;FBDV/Android SDK built for x86;FBMD/x86;FBSN/;FBSV/7.0;FBSS/Android 7.0;FBCA/armeabi-v7a:x86;]"
        ua3 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/HTC;FBDV/Android SDK built for x86;FBMD/x86;FBSN/;FBSV/7.0;FBSS/Android 7.0;FBCA/armeabi-v7a:x86;]"
        ua4 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/Xiaomi;FBDV/Android SDK built for x86;FBMD/x86;FBSN/;FBSV/8.0.0;FBSS/Android 8.0.0;FBCA/armeabi-v7a:x86;]"
        ua5 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBDM/{density=2
