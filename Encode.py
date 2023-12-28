
#color
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"
#imports
import time, os, sys, random
from os import system as sm
from sys import platform as pf
from time import sleep as sp

print(" \033[1;33mWELCOME TO GREIGOR'S USER AGENT GENERATOR ")
sp(1.5)


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#________________________________________#

logo=(f"""{GREEN}

       
                   ██████╗███╗   ███╗███████╗
                  ██╔════╝████╗ ████║██╔════╝
                  ╚█████╗ ██╔████╔██║█████╗
                   ╚═══██╗██║╚██╔╝██║██╔══╝
                  ██████╔╝██║ ╚═╝ ██║██║
                  ╚═════╝ ╚═╝     ╚═╝╚═╝
                                        
{WHITE}================================================================
[•] NAME         : YUJI GREIGOR 
[•] FACEBOOK     : https://www.facebook.com/Yuji.IAmLimitless
[•] TOOL         : USER AGENT GENERATOR 
[•] VERSION      : 1.0
{WHITE}================================================================""")
def linex():
    print('\033[1;37m================================================================')
sm("mkdir /sdcard/UA-GEN")
#clear
def clear():
    if pf in ["win32","win64"]:
        sm("cls")
    else:
        sm("clear")
    print(logo)
#menu
fb = []
def main():
    clear()
    print("[1] VIVO ")
    print("[2] XIAOMI ")
    print("[3] SAMSUNG ")
    print("[4] OPPO ")
    print("[5] TECNO ")
    print("[6] INFINIX ")
    print("[0] EXIT ")
    linex()
    select = input("CHOOSE AN OPTION: ")
    if select == "1":
        vivo()
    elif select == "2":
        xiaomi()
    elif select == "3":
        samsung()
    elif select == "4":
        oppo()
    elif select == "5":
        tecno()
    elif select == "6":
    	infinix()
    elif select == "0":
        sys.exit(f"BYE")
    else:
        exit()
#+++++++++++++VIVO++++++++++++#
def vivo():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    print("[4] DALVIK WITH FBAN ")
    print("[5] DOUBLE USER AGENT ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    elif fban == "3":
        fb.append("3")
    elif fban == "4":
    	fb.append("4")
    else:
        fb.append("5")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 VivoBrowser/"+str(random.randrange(5,11))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/en_PH;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/en_PH;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 13; 22081212UG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 9; V1814A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 10; V1838A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 5.0.2; vivo X5Pro D Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android 4.4.4; vivo X5Max) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 11; V2085A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20Plus A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 11; V2149 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "4" in fb:
        for i in range(num):
            ua = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "5" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    else:
        exit()
#++++++++++++++++XIAOMI++++++++++++++#        
def xiaomi():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    print("[4] DALVIK WITH FBAN ")
    print("[5] DOUBLE USER AGENT ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    elif fban == "3":
        fb.append("3")
    elif fban == "4":
    	fb.append("4")
    else:
        fb.append("5")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 AlohaBrowser/"+str(random.randrange(5,11))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_PH;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/en_PH;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 13; 22081212UG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 12; 21061119BI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 10; M2004J7BC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android 13; 23106RN0DA Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N9002) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5pro Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 8.1; Redmi 6Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "4" in fb:
        for i in range(num):
            ua = "Dalvik/2.1.0 (Linux; U; Android 9; Xiaomi Redmi Note 7 Build/PI) [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.katana;FBLC/en_PH;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "5" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    else:
        exit()
#+++++++++++++++SAMSUNG+++++++++++++++#        
def samsung():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    print("[4] DALVIK WITH FBAN ")
    print("[5] DOUBLE USER AGENT ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    elif fban == "3":
        fb.append("3")
    elif fban == "4":
    	fb.append("4")
    else:
        fb.append("5")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-N960N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/"+str(random.randrange(5,11))+" Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_PH;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua1 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A52s;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua2 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix ;FBDV/Samsung A7;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua3 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/SAMSUNG SM-N9810;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua4 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_PH;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N985F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            ua5 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/SM-N986U1;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua6 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/SAMSUNG SM-N900S;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua7 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9002;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua8 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/GT-N7105T;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua9 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/Galaxy Note20;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua10 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G5528;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 5.0; Samsung A52s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 8.1.1; Samsung A7 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N9810) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 11; SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android 10; SM-N986U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 4.4.2; en-gb; SAMSUNG SM-N900S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N9002) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 4.1.1; GT-N7105T Build/JRO03C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 10; Galaxy Note20 Build/QD4A.200805.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G5528 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "4" in fb:
        for i in range(num):
            ua = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "5" in fb:
        for i in range(num):
            ua1 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A52s;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua2 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix ;FBDV/Samsung A7;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua3 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/SAMSUNG SM-N9810;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua4 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_PH;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N985F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            ua5 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/SM-N986U1;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua6 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/SAMSUNG SM-N900S;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua7 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9002;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua8 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/GT-N7105T;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua9 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBDV/Galaxy Note20;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua10 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G5528;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    else:
        exit()
#+++++++++++++++OPPO++++++++++++++#        
def oppo():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    print("[4] DALVIK WITH FBAN ")
    print("[5] DOUBLE USER AGENT ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    elif fban == "3":
        fb.append("3")
    elif fban == "4":
    	fb.append("4")
    else:
        fb.append("5")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 OppoBrowser/"+str(random.randrange(5,11))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+"."+str(random.randrange(1,9))+" [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_PH;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_PH;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 10; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 13; PHQ110 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 11; CPH2271 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 5.1.1; OPPO A33m Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android 10; CPH2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 7.1.1; OPPO A77) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 9; PBBM00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 11; CPH2059) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 8.1.0; CPH1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "4" in fb:
        for i in range(num):
            ua = "Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "5" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    else:
        exit()
#+++++++++++++++TECNO+++++++++++++#        
def tecno():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    else:
        fb.append("3")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua = "Mozilla/5.0 (Linux; Android 10; TECNO KC8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_PH;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_PH;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 7.1; Tecno A602) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 9; TECNO AB7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 12; TECNO AD9 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 8.1.0; TECNO BA2 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua5 = "Mozilla/5.0 (Linux; Android 5.0.2; TECNO-C8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 9; TECNO CC9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 11; TECNO CH6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 13; TECNO CK7n Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 7.0; TECNO CX Air) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 8.1.0; TECNO ID3k) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    else:
        exit()
#+++++++++++++++INFINIX+++++++++++++#        
def infinix():
    clear()
    print("[1] MOZILLA WITH FBAN ")
    print("[2] FBAN ONLY ")
    print("[3] MOZILLA ONLY ")
    print("[4] DALVIK WITH FBAN ")
    print("[5] DOUBLE USER AGENT ")
    linex()
    fban = input("CHOOSE AN OPTION: ")
    if fban == "1":
        fb.append("1")
    elif fban == "2":
        fb.append("2")
    elif fban == "3":
        fb.append("3")
    elif fban == "4":
    	fb.append("4")
    else:
        fb.append("5")
    linex()
    num = int(input("HOW MANY UA DO YOU WANT TO GENERATE? "))
    linex()
    if "1" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X606B;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua2 = "Mozilla/5.0 (Linux; Android 7.0; Infinix X559 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X559;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua3 = "Mozilla/5.0 (Linux; Android 11; Infinix X698) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X698;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua4 = "Mozilla/5.0 (Linux; Android 12; Infinix X671 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";] [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X671;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua5 = "Mozilla/5.0 (Linux; Android 12; Infinix X6820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X6820;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua6 = "Mozilla/5.0 (Linux; Android 11; Infinix X6811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix ;FBDV/Infinix X6811;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua7 = "Mozilla/5.0 (Linux; Android 11; Infinix X6810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6810;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua8 = "Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X620;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua9 = "Mozilla/5.0 (Linux; Android 11; Infinix X663D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X663D;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua10 = "Mozilla/5.0 (Linux; Android 5.1; Infinix X506) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X506;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "2" in fb:
        for i in range(num):
            ua1 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X606B;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua2 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X559;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua3 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X698;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua4 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X671;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua5 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X6820;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua6 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix ;FBDV/Infinix X6811;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua7 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6810;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua8 = "[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X620;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua9 = "[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X663D;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua10 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X506;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "3" in fb:
        for i in range(num):
            ua1 = "Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua2 = "Mozilla/5.0 (Linux; Android 7.0; Infinix X559 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua3 = "Mozilla/5.0 (Linux; Android 11; Infinix X698) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua4 = "Mozilla/5.0 (Linux; Android 12; Infinix X671 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";]"
            ua5 = "Mozilla/5.0 (Linux; Android 12; Infinix X6820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua6 = "Mozilla/5.0 (Linux; Android 11; Infinix X6811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua7 = "Mozilla/5.0 (Linux; Android 11; Infinix X6810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua8 = "Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua9 = "Mozilla/5.0 (Linux; Android 11; Infinix X663D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            ua10 = "Mozilla/5.0 (Linux; Android 5.1; Infinix X506) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(73,117))+".0."+str(random.randrange(3000,5800))+"."+str(random.randrange(40,150))+" Mobile Safari/537.36"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    elif "4" in fb:
        for i in range(num):
            ua = "Dalvik/2.1.0 (Linux; U; Android 10; Infinix X688B Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            sp(0.5)
            print(f"FRESH UA {i+1}: {ua}\n")
    elif "5" in fb:
        for i in range(num):
            ua1 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X606B;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua2 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X559;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua3 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X698;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua4 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X671;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua5 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X6820;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua6 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix ;FBDV/Infinix X6811;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua7 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6810;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            ua8 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.orca;FBLC/en_PH;FBBV/396116327;FBCR/TNT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X620;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]"
            ua9 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/MessengerLite;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBPN/com.facebook.mlite;FBLC/en_PH;FBBV/346850586;FBCR/TNT;FBMF/INFINIX MOBILTY LIMITED;FBBD/Infinix;FBDV/Infinix X663D;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};]"
            ua10 = "[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";[FBAN/FB4A;FBAV/"+str(random.randrange(70,400))+".0.0."+str(random.randrange(10,77))+"."+str(random.randrange(40,200))+";FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_PH;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X506;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            possible_ua = [ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10] 
            chosen_ua = random.choice(possible_ua)
            sp(0.5)
            print(f"FRESH UA {i+1}: {chosen_ua}\n")
    else:
        exit()
#end
main()
