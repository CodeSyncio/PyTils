import __main__
from colorama import Fore
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def FileSpam():
        cls()
        
        print(Fore.MAGENTA+"File Amount?")
        amount = input()
        print(Fore.MAGENTA+"File Names?")
        fname = input()
        print(Fore.MAGENTA+"text in file?")
        fcontent = input()
        print(Fore.MAGENTA+"File Extensions?")
        ext = input()
        
        curam = 1
        while int(curam)<=int(amount):
            
            if curam %100==0:
                cls()
                filledam = round(curam /int(amount) * 50)
                nonfilledam = 50-filledam
                print(Fore.LIGHTCYAN_EX+f'[{filledam*"█"}{nonfilledam*"-"}]    [{curam /int(amount) *100}%]')
                
            file = open(f'{str(fname)}{str(curam)}.{str(ext)}','w')
            file.write(fcontent)
        
            curam = curam+1
        print(Fore.MAGENTA+"DONE")
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to spam more files")
        ghinput = input()
        if ghinput =='':
            mainscrn()
        else:
            FileSpam()