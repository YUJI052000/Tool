import os
import time
import marshal
import compile

GREEN = '\033[1;32m'
WHITE = '\033[1;97m'

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

def linex():
    print('\033[1;37m================================================================')

def main():
    os.system('clear')
    print(logo)
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
