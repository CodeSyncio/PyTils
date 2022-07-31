import __main__
from colorama import Fore
import os,time
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()

def ModifyOPTS():
        cls()
        if os.path.exists('OPT/SDREQ.exe'):
            MPEGstatus = True
        else:
            MPEGstatus = False
        print(Fore.CYAN+"This is a list of currently installed dependencies:")
        if MPEGstatus is True:
            print(Fore.GREEN+"[1] Spotify Downloader dependency [INSTALLED]")
        else:
            print(Fore.RED+"[1] Spotify Downloader dependency [NOT INSTALLED]")
        
        print(Fore.MAGENTA+"\nType the number of the corresponding dependency you wanna DELETE to delete it, press enter to go back to the main menu.")
        modoptschoise = input()
        if modoptschoise == '1':
            try:
                os.remove(f'{os.getcwd()}/OPT/SDREQ.exe')
                print(Fore.GREEN+'Sucessfully uninstalled the Spotify Downloader dependency\nreturning to main screen...')
                time.sleep(3)
                mainscrn()
            except:
                print(Fore.RED+'the Spotify Downloader dependency could not be found / deleted, sorry\nreturning to main screen...')
                time.sleep(3)
                mainscrn()
        
        if modoptschoise == '':
             mainscrn()