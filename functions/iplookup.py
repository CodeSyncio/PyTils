import __main__
from colorama import Fore
import colorama
import requests
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()

    
def IpLookup():
        LookUpOpts =    ['ip',
                        'region',
                        'city',
                        'organisation',
                        'rawlocation',
                        'postalcode',
                        'timezone',
                        'anycaststatus',
                        'country']
    
        IpInfoLookupVals =['ip',
                       'region',
                       'city',
                       'org',
                       'loc',
                       'postal',
                       'timezone',
                       'anycast',
                       'country']
        
        cls()
        print(Fore.MAGENTA+"Ip / Host to check:")
        ip = str(input())
        if ip=='':
            __main__.init.MainScreen()
        data = requests.get(f'https://ipinfo.io/{ip}/json').json()
        try:
            data.pop('readme')
        except:
            pass
        for i in range(len(LookUpOpts)):
            try:
                print(Fore.CYAN+f"{LookUpOpts[i]} = "+Fore.LIGHTCYAN_EX+f"{data[IpInfoLookupVals[i]]}")
            except:
                pass
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to lookup another host")
        ghinput = input()
        if ghinput =='':
            mainscrn()
        else:
            IpLookup()