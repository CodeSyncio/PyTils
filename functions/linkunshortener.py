import __main__
from colorama import Fore
import requests,time
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def unshorten():
        cls()
        print(Fore.CYAN+'Please enter the shortened link:')
        shortlink = input()
        
        print(Fore.MAGENTA+'working...')
        try:
            unshortlink = requests.get(f'https://unshorten.me/json/{shortlink}').json()
            if unshortlink["success"] == True:
                print(Fore.GREEN+'Sucess!')
                print(Fore.CYAN+f'Unshortened link: {unshortlink["resolved_url"]}')
                print(Fore.MAGENTA+"\nPress enter to return to the main menu ,any other key to unsorten another link")
                ghinput = input()
                if ghinput =='':
                    mainscrn()
                else:
                    unshorten()  
            else:
                print(Fore.RED+'Sorry, that link is not valid. returning to main menu in 2 secs...')
                time.sleep(2)
                mainscrn()
        except:
            print(Fore.RED+'sorry, please report this error to CodeSyncio.returning')
            time.sleep(2)
            mainscrn()
        