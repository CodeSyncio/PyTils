import __main__
from colorama import Fore
from subprocess import DEVNULL,STDOUT
import os,time,ctypes,sys
from ctypes import *
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()

def getadmin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def SystemRepair():
        cls()
        
        if getadmin() ==1:
            print(Fore.MAGENTA+"Correct permissions! starting repair...")
            print(Fore.MAGENTA+"[Phase 1/2]")
            os.system("sfc /scannow")
            cls()
            print(Fore.MAGENTA+"[Phase 2/2]")
            os.system("DISM /Online /Cleanup-Image /RestoreHealth /Source:repairSource\install.wim")
            cls()
            print(Fore.MAGENTA+"Repairs are done.")
            print(Fore.CYAN+"A reboot is recommended to avoid issues. Reboot now? [y/n]")
            rebchoise = input()
            if rebchoise =="y":
                cls()
                print(Fore.MAGENTA+"Rebooting in 5 seconds...")
                time.sleep(5)
                os.system("shutdown /r /t 1")   
                print(Fore.MAGENTA+"REBOOTING")
                os._exit(1)
            else:
                mainscrn()
        else:
            print(Fore.LIGHTRED_EX+"System Repair requires admin permissions!")
            print(Fore.CYAN+"Restart program with admin permissions? [y/n]")
            achoise = input()
            if achoise =="y":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                os._exit(1)
            else:
                mainscrn()