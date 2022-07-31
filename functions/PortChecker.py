import __main__
import socket
from colorama import Fore
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()


def CheckPort():
        cls()
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        print(Fore.MAGENTA+"\n\nIp / Host to check port status on:")
        ip = str(input())
        if ip=='':
            mainscrn()
        print(Fore.MAGENTA+f"port to check of {ip}:")
        port = int(input())
        result = s.connect_ex((ip,port))
        s.close()
        
        if result ==0:
            print(Fore.LIGHTGREEN_EX+f"Port {port} is open at host {ip}")
        else:
            print(Fore.LIGHTRED_EX+f"Port {port} is CLOSED at host {ip}")
        
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to recheck another host")    
        ghinput = input()
        if ghinput =='':
            mainscrn()
        else:
            CheckPort()