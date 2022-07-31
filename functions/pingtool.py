import __main__
from colorama import Fore
from subprocess import DEVNULL,STDOUT
import subprocess
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def ping():
        cls()
        print(Fore.MAGENTA+"Ip / Host to ping:")
        ip = input()
        if ip=='':
            mainscrn()
        def pingprocess(ip):
            cmd = f'ping -n 1 {ip}'
        
            if subprocess.call(cmd,stdout=DEVNULL, stderr=subprocess.STDOUT) == 0:
                print(Fore.LIGHTGREEN_EX+f"Target {ip} is ALIVE")
            else:
                print(Fore.LIGHTRED_EX+f"Target {ip} is UNREACHABLE")
            print(Fore.MAGENTA+"Press enter to return to REPING , any other key to go to the main menu")
            ghinput = input()
        
            if ghinput =='':
                pingprocess(ip)
            else:
                mainscrn()
            
        pingprocess(ip)