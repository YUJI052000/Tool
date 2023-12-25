import marshal,os,sys,time

    
#++++++++++++++COLORS+++++++++++++#
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
#++++++++++++LOGO+++++++++++++#

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
[•] TOOL         : ENCODER/ENCRYPTER 
[•] VERSION      : 1.0
{WHITE}================================================================""")
#++++++++++LINEX++++++++#
def linex():
    print('\033[1;37m================================================================')
def main():
        try:
        	    os.system('clear')
                print (logo)
                print (' EXAMPLE: /sdcard/yuji.py ')
                file = input (' FILE NAME: ')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = (' # ENCODE BY : YUJI GREIGOR\n# ENCRYPTION : PY3 MARSHAL\n# TOOL VERSION : 1.0\nimport marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                print (' SUCCESSFULLY ENCRYPTION : ')
                linex()
                time.sleep(1)
                aq = input (' YOU WANT TO ENCRYPT AGAIN? (y/n) ')
                if aq =="":
                        print (' INVALID ')
                        os.sys.exit()
                elif aq =="y" or aq =="Y":
                        main()
                else:
                        if aq =="n" or aq =="N":
                                print (' THANK YOU FOR USING IT!!! ')
                        else:
                                print (' INVALID. TRY AGAIN ')
                                os.sys.exit()
        except IOError:
                print (' FILE NOT FOUND ')
                time.sleep(1)
                main()

if __name__=='__main__':
        main()
