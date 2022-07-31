#<---VERSION HEADER--->
FileVersion = "v0.1.0"           
FileName = "first public release :0"   

#<---importing fucntions /selfbot / dependency manager--->
from functions import BlueScreenOfDeath,mygithub, WhatIsMyIp, filespammer, linkunshortener, pingtool,iplookup,PortChecker,base, spotifydownloader, systemrepair, youtubedownloader
from DepManager import DependencyManager
from discordbot import selfbot

#<---extra imports--->
import  os
from multiprocessing import Process,Queue
import ctypes
import colorama
from colorama import *
from colorama import init, Fore,Style
import os
import requests
import time
import json


#<---console title--->
ctypes.windll.kernel32.SetConsoleTitleW("PyTils - CodeSyncio.github.io (づ ◕‿◕ )づ")

#<---colorama initiation--->
colorama.init(autoreset = True)

#<---utility functions--->
class util():
    def cls():                                         
        os.system('cls' if os.name=='nt' else 'clear')    
        
    def LoadToken():
        with open('config.json','r') as cf:
            settings = []
            settings.append(json.load(cf))
            return settings[0]['discordtoken']
      
#<----------startup functions---------->
class init():
    def CheckValidy():
        
        #<---checking required folders/files--->
        if os.path.exists('OPT'):
            pass
        else:         
            os.mkdir('OPT')
        if os.path.exists('TEMP'):
            pass
        else:   
            os.mkdir('TEMP')
        if os.path.exists('config.json'):
            pass
        else:
            with open('config.json', 'w') as outfile:
                template = {"discordtoken": "TokenHere"}
                json.dump(template, outfile)
                outfile.close()

        #<---starting bot process with token from config--->
        botsubprocess = Process(target=selfbot.SelfBot,args=(util.LoadToken(),q)).start()
        
        #<---checking if the file's version is supported--->
        print(Fore.MAGENTA+"Checking Version header...")
        try:
            CurrentlySupportedVersions =requests.get('https://pastebin.com/raw/JKcW9Gdv' ).text  
        except:
            print(Fore.LIGHTRED_EX+"Oops! Seems like no connection could be make to the Version Header database :( Quitting...")
            time.sleep(2)
            os._exit(1)
        lines = CurrentlySupportedVersions.splitlines()
        for line in lines:
            if FileVersion == line.strip():
                print(Fore.LIGHTGREEN_EX+"Version header is valid! starting mainfuction...")
                time.sleep(2)
                init.MainScreen()
            else:
                pass
        print(Fore.LIGHTRED_EX+"Version header is INVALID! quitting...")
        time.sleep(2)
        os._exit(1)
    
    #<---main landing screen--->
    def MainScreen():
        
        util.cls()
        print(Fore.BLUE+r'''
                ______   _______ ___ _     ____  
                |  _ \ \ / /_   _|_ _| |   / ___| 
                | |_) \ V /  | |  | || |   \___ \ 
                |  __/ | |   | |  | || |___ ___) |
                |_|    |_|   |_| |___|_____|____/      ''')
        
        print(Fore.CYAN+'<----------Tools---------->')
        print(Fore.LIGHTBLUE_EX+"[1] Ping")
        print(Fore.LIGHTBLUE_EX+"[2] Ip Info Lookup")
        print(Fore.LIGHTBLUE_EX+"[3] Ip Port Checker")
        print(Fore.LIGHTBLUE_EX+"[4] Base64 ENCODE")
        print(Fore.LIGHTBLUE_EX+"[5] Base64 DECODE")
        print(Fore.LIGHTBLUE_EX+"[6] File Spammer")
        print(Fore.LIGHTBLUE_EX+"[7] System Repair")
        print(Fore.LIGHTBLUE_EX+"[8] Raise BSOD (testing purposes)")
        print(Fore.LIGHTBLUE_EX+"[9] What's my ip")
        print(Fore.LIGHTBLUE_EX+"[10] Youtube downloader")
        print(Fore.LIGHTBLUE_EX+"[11] Spotify downloader")
        print(Fore.LIGHTBLUE_EX+"[12] link unshortener")
        print(Fore.LIGHTBLUE_EX+"[13] My Site")
        print(Fore.LIGHTBLUE_EX+"[14] modify installed dependencies")
        print(Fore.CYAN+'<----------Discord Selfbot---------->')
        if q.empty() is True:
            print(Fore.GREEN+('Bot is running'))
            print(Fore.LIGHTBLUE_EX+'[15] Bot commands')
        else:
            print(Fore.RED+'Bot is not running')
        print(Fore.MAGENTA+"\n\nPlease choose an option.")
        print(Fore.MAGENTA+"Option:")
        
        choiseMainScreen = str(input())
        match choiseMainScreen :
            case '1':
                pingtool.ping(),
            case '2':
                iplookup.IpLookup(),
            case '3':
                PortChecker.CheckPort(),    
            case '4':
                base.b64enc(),
            case '5':
                base.b64dec(),
            case '6':
                filespammer.FileSpam(),
            case '7':
                systemrepair.SystemRepair(),
            case '8':
                BlueScreenOfDeath.InstantBSOD(),
            case '9':
                WhatIsMyIp.WhatIsMyIp(),
            case '10':
                youtubedownloader.ytdownloader(),
            case '11':
                spotifydownloader.spotdowload(),
            case '12':
                linkunshortener.unshorten(),
            case '13':
                mygithub.MyGit(),
            case '14':
                DependencyManager.ModifyOPTS(),
            case '15':
                selfbot.botinfo(),
            case '':
                init.MainScreen(),
            
#<----------START----------> 
if __name__ == '__main__':
    global q
    q = Queue()
    init.CheckValidy()