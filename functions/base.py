import __main__
from colorama import Fore
from subprocess import DEVNULL,STDOUT

import base64
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
    
   
def b64enc():
    cls()
    print(Fore.BLUE+"---BASE64_ENCODE---")
    print(Fore.MAGENTA+"\n\nText to convert:")
    encinput = str(input())
    out = base64.b64encode(encinput.encode('utf-8'))
    
    
    print(Fore.MAGENTA+ "Encoded text:")
    print (str(Fore.LIGHTCYAN_EX+str(out,encoding='utf-8')))
    print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to encode more text")    
    ghinput = input()
    if ghinput =='':
        mainscrn()
    else:
        b64enc()

   
def b64dec():
    cls()
    print(Fore.BLUE+"---BASE64_DECODE---")
    print(Fore.MAGENTA+"\n\nEncoded input:")
    encinput = str(input())
    out = base64.b64decode(encinput.encode("utf-8"))
    print(Fore.MAGENTA+ "Decoded text:")
    print(Fore.LIGHTCYAN_EX+str(out,encoding='utf-8'))
    print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to decode more text")
    ghinput = input()
    if ghinput =='':
        mainscrn()
    else:
        b64dec()