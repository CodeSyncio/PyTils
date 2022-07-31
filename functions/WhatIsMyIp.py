import __main__
from colorama import Fore
import socket,requests
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def WhatIsMyIp():
        cls()
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)
        print(Fore.CYAN+f'Your public ip: {requests.get("http://api.ipify.org/?format=text").text}')
        print(Fore.CYAN+f'Your private ip: {IPAddr}')

        print(Fore.MAGENTA+"\nPress enter to return to the main menu")
        ghinput = input()
        mainscrn()