#<---VERSION HEADER--->
FileVersion = "v0.1.0"           
FileName = "first public release :0"   

#<---imports--->
import asyncio
import sys, os
from multiprocessing import Process,Queue
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup
from pytube import YouTube
from webbrowser import open_new
import ctypes
import socket
from socket import timeout
import colorama
from colorama import *
from colorama import init, Fore,Style
import os
import subprocess
from subprocess import DEVNULL,STDOUT
import requests
import time
import base64
import sys
import json
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
from discord.ext import commands
import discord

#<---console title--->
ctypes.windll.kernel32.SetConsoleTitleW("PyTils - CodeSyncio.github.io (づ ◕‿◕ )づ")

#<---colorama initiation--->
colorama.init(autoreset = True)

#<----------tables---------->
class tables():
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
    
#<---utility functions--->
class util():
    def cls():                                         
        os.system('cls' if os.name=='nt' else 'clear')    
        
    def getadmin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
        
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
                template = {
                                "discordtoken": "TokenHere"
                                }
                json.dump(template, outfile)
                outfile.close()
                
        #<---starting bot process with token from config--->
        botsubprocess = Process(target=discordbotting.SelfBot,args=(util.LoadToken(),q)).start()
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
                functions.ping(),
            case '2':
                functions.IpLookup(),
            case '3':
                functions.CheckPort(),    
            case '4':
                functions.b64enc(),
            case '5':
                functions.b64dec(),
            case '6':
                functions.FileSpam(),
            case '7':
                functions.SystemRepair(),
            case '8':
                functions.InstantBSOD(),
            case '9':
                functions.WhatIsMyIp(),
            case '10':
                functions.ytdownloader(),
            case '11':
                functions.spotdowload(),
            case '12':
                functions.unshorten(),
            case '13':
                functions.MyGit(),
            case '14':
                functions.ModifyOPTS(),
            case '15':
                discordbotting.botinfo(),
            case '':
                init.MainScreen(),
            
            
#<---tool functions--->           
class functions():
    #<---ping tool--->
    def ping():
        util.cls()
        print(Fore.MAGENTA+"\n\nIp / Host to ping:")
        ip = input()
        if ip=='':
            init.MainScreen()
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
                init.MainScreen()
            
        pingprocess(ip)
    
    #<---ip info tool--->        
    def IpLookup():
        util.cls()
        print(Fore.MAGENTA+"\n\nIp / Host to check:")
        ip = str(input())
        if ip=='':
            init.MainScreen()
        data = requests.get(f'https://ipinfo.io/{ip}/json').json()
        try:
            data.pop('readme')
        except:
            pass
        for i in range(len(tables.LookUpOpts)):
            try:
                print(Fore.CYAN+f"{tables.LookUpOpts[i]} = "+Fore.LIGHTCYAN_EX+f"{data[tables.IpInfoLookupVals[i]]}")
            except:
                pass
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to lookup another host")
        ghinput = input()
        if ghinput =='':
            init.MainScreen()
        else:
            functions.IpLookup()
    
    #<---port status tool--->
    def CheckPort():
        util.cls()
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        print(Fore.MAGENTA+"\n\nIp / Host to check port status on:")
        ip = str(input())
        if ip=='':
            init.MainScreen()
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
            init.MainScreen()
        else:
            functions.CheckPort()
    
    #<---base64 text encoder--->    
    def b64enc():
        util.cls()
        print(Fore.BLUE+"---BASE64_ENCODE---")
        print(Fore.MAGENTA+"\n\nText to convert:")
        encinput = str(input())
        out = base64.b64encode(encinput.encode('utf-8'))
        
        
        print(Fore.MAGENTA+ "Encoded text:")
        print (str(Fore.LIGHTCYAN_EX+str(out,encoding='utf-8')))
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to encode more text")    
        ghinput = input()
        if ghinput =='':
            init.MainScreen()
        else:
            functions.b64enc()
    
    #<---base64 decoder--->    
    def b64dec():
        util.cls()
        print(Fore.BLUE+"---BASE64_DECODE---")
        print(Fore.MAGENTA+"\n\nEncoded input:")
        encinput = str(input())
        out = base64.b64decode(encinput.encode("utf-8"))
        print(Fore.MAGENTA+ "Decoded text:")
        print(Fore.LIGHTCYAN_EX+str(out,encoding='utf-8'))
        print(Fore.MAGENTA+"Press enter to return to the main menu ,any other key to decode more text")
        ghinput = input()
        if ghinput =='':
            init.MainScreen()
        else:
            functions.b64dec()

    #<---file spammer--->
    def FileSpam():
        util.cls()
        
        print(Fore.MAGENTA+"\n\nFile Amount?")
        amount = input()
        print(Fore.MAGENTA+"\n\nFile Names?")
        fname = input()
        print(Fore.MAGENTA+"\n\ntext in file?")
        fcontent = input()
        print(Fore.MAGENTA+"\n\nFile Extensions?")
        ext = input()
        
        curam = 1
        while int(curam)<=int(amount):
            
            if curam %100==0:
                util.cls()
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
            init.MainScreen()
        else:
            functions.FileSpam()
    
    #<---system repair tool--->        
    def SystemRepair():
        util.cls()
        if util.getadmin():
            print(Fore.MAGENTA+"Correct permissions! starting repair...")
            print(Fore.MAGENTA+"[Phase 1/2]")
            os.system("sfc /scannow")
            util.cls()
            print(Fore.MAGENTA+"[Phase 2/2]")
            os.system("DISM /Online /Cleanup-Image /RestoreHealth /Source:repairSource\install.wim")
            util.cls()
            print(Fore.MAGENTA+"Repairs are done.")
            print(Fore.CYAN+"A reboot is recommended to avoid issues. Reboot now? [y/n]")
            rebchoise = input()
            if rebchoise =="y":
                util.cls()
                print(Fore.MAGENTA+"Rebooting in 5 seconds...")
                time.sleep(5)
                os.system("shutdown /r /t 1")   
                print(Fore.MAGENTA+"REBOOTING")
                os._exit(1)
            else:
                init.MainScreen()
        else:
            print(Fore.LIGHTRED_EX+"System Repair requires admin permissions!")
            print(Fore.CYAN+"Restart program with admin permissions? [y/n]")
            achoise = input()
            if achoise =="y":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                os._exit(1)
            else:
                init.MainScreen()
    
    #<---bsod without admin tool--->    
    def InstantBSOD():
        util.cls()
        print(Fore.LIGHTRED_EX+"WARNING: this will INSTANTLY crash your system! only use this for testing! continue? [y/n]")
        bsodinput = input()
        if bsodinput == "y":
            print(Fore.LIGHTRED_EX+"CRASHING...")
            nullptr = POINTER(c_int)()
            windll.ntdll.RtlAdjustPrivilege(c_uint(19) , c_uint(1) , c_uint(0) , byref(c_int()))
            windll.ntdll.NtRaiseHardError(c_ulong(0xC000007B) , c_ulong(0) , nullptr , nullptr , c_uint(6) , byref(c_uint()))
        else:
            init.MainScreen()
    
    #<---current local/public ip tool--->        
    def WhatIsMyIp():
        util.cls()
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)
        print(Fore.CYAN+f'Your public ip: {requests.get("http://api.ipify.org/?format=text").text}')
        print(Fore.CYAN+f'Your private ip: {IPAddr}')

        print(Fore.MAGENTA+"\nPress enter to return to the main menu")
        ghinput = input()
        init.MainScreen()
    
    #<---opens my github--->
    def MyGit():
        open_new('https://codesyncio.github.io')
        init.MainScreen()

    #<---youtube downloader--->
    def ytdownloader():
        if os.path.exists('youtube-downloads'):
            pass
        else:
                    
            os.mkdir('youtube-downloads')
        util.cls()
        
        def on_progresscheck(stream, chunk: bytes, bytes_remaining: int):
            current = ((stream.filesize - bytes_remaining)/stream.filesize)
            progress = int(50*current)
            status = '█' * progress + '-' * (50 - progress)
            
            sys.stdout.write(Fore.LIGHTCYAN_EX+f'--> |{status}| {round(current*100)} %\r')
            sys.stdout.flush()
            
        print(Fore.CYAN+"Please enter the yt link:")
        
        link = input()
        if link=='':
            init.MainScreen()
        yt = YouTube(link,on_progress_callback=on_progresscheck)
        vt = yt.title
        ys = yt.streams.get_highest_resolution()
        size = round(ys.filesize/1000000)
        util.cls()
        print(Fore.MAGENTA+f"Starting download of video [{vt}]  ({size} MB)")
        ys.download(output_path=f'{os.getcwd()}/youtube-downloads/')
        print(Fore.GREEN+f"\nSucessfully downloaded {vt}, file is saved in the 'youtube-downloads' folder")
        
        print(Fore.MAGENTA+"\nPress enter to return to the main menu ,any other key to download another video")
        ghinput = input()
        if ghinput =='':
            init.MainScreen()
        else:
            functions.ytdownloader()
    
    #<---spotify downloader--->
    def spotdowload():
        if os.path.exists('spotify-downloads'):
            pass
        else:       
            os.mkdir('spotify-downloads')
        util.cls()
        
        if os.path.exists(f'{os.getcwd()}/OPT/SDREQ.exe'):
            print(Fore.GREEN+"Dependency found!")
            pass
        else:
            print(Fore.RED+"A required dependency for this utility was not found, download it now? [y/n]")
            depchoise = input()
            if depchoise == 'y':
                depreq = requests.get('https://github.com/CodeSyncio/Pytils-optional-dependencies/raw/main/SDREQ.exe')
                if os.path.exists('OPT'):
                    pass
                else:
                    os.mkdir('OPT')
                open(f'{os.getcwd()}\\OPT\\SDREQ.exe', 'wb').write(depreq.content)
            else:
                init.MainScreen()
        print(Fore.CYAN+"Please enter the song link:")
        implink = input()
        if implink=='':
            init.MainScreen()
        req = requests.get(implink)
        soup = BeautifulSoup(req.text,'html.parser')
        title = soup.find('meta', property='og:title',content=True)
        artist_link = soup.find('meta', property="music:musician",content=True)
        artist_page = BeautifulSoup(requests.get(artist_link['content']).text,'html.parser')
        artist_name = artist_page.find('meta', property='og:title')
        song = title['content']
        artist =  artist_name['content']
        song_name = str(song + " " + artist) 
        ytquery = song_name.replace(" ", "+")
        results = list(YoutubeSearch(str(ytquery), max_results=1).to_dict())[-1]
        resultsurlsuffix = str(results['url_suffix'])
        
        print(Fore.GREEN+"Song found")
        print(Fore.MAGENTA+"Starting download")
        
        def on_progresschecksf(stream, chunk: bytes, bytes_remaining: int):
            current = ((stream.filesize - bytes_remaining)/stream.filesize)
            progress = int(50*current)
            status = '█' * progress + '-' * (50 - progress)
            sys.stdout.write(Fore.LIGHTCYAN_EX+f'--> |{status}| {round(current*100)} %\r')
            sys.stdout.flush()
        
        yt =YouTube(f"https://www.youtube.com/{resultsurlsuffix}",on_progress_callback=on_progresschecksf)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=f"{os.getcwd()}/TEMP")
        
        name = ys.default_filename
        out = ys.title
        subprocess.run([
        f'{os.getcwd()}/OPT/SDREQ',
        '-i', os.getcwd()+'/TEMP/'+name,
         os.getcwd()+'/spotify-downloads/'+out+".mp3"
        ],stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT)
        
        os.remove(f"{os.getcwd()}/TEMP/{name}")
        
        print(Fore.LIGHTGREEN_EX+"\nDownload Completed!")
        print(Fore.MAGENTA+"\nsongs get saved in the 'spotify-downloads' folder")     
        print(Fore.MAGENTA+"\nPress enter to return to the main menu ,any other key to download another spotify song")
        ghinput = input()
        if ghinput =='':
            init.MainScreen()
        else:
            functions.spotdowload()     
    #<---link unshortening tool--->    
    def unshorten():
        util.cls()
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
                    init.MainScreen()
                else:
                    functions.unshorten()  
            else:
                print(Fore.RED+'Sorry, that link is not valid. returning to main menu in 2 secs...')
                time.sleep(2)
                init.MainScreen()
        except:
            print(Fore.RED+'sorry, please report this error to CodeSyncio.returning')
            time.sleep(2)
            init.MainScreen()
        
    
    
    
    
    #<---tool dependency manager--->
    def ModifyOPTS():
        util.cls()
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
                init.MainScreen()
            except:
                print(Fore.RED+'the Spotify Downloader dependency could not be found / deleted, sorry\nreturning to main screen...')
                time.sleep(3)
                init.MainScreen()
        
        if modoptschoise == '':
             init.MainScreen()

#<---discord selfbot(s)---> 
class discordbotting():
    def SelfBot(tokywoky,q):
        bot = commands.Bot(command_prefix='§', self_bot=True)
        
        #<---command defining---> 
        @bot.command()
        async def shrug(ctx):
            await ctx.message.delete()
            await ctx.send("¯\_(ツ)_/¯")
            
        @bot.command()
        async def disapprove(ctx):
            await ctx.message.delete()
            await ctx.send("ᇂ_ᇂ")
            
        @bot.command()
        async def fu(ctx):
            await ctx.message.delete()
            await ctx.send("( ͡° ͜つ ͡°)╭∩╮")
        
        @bot.command()
        async def confused(ctx):
            await ctx.message.delete()
            await ctx.send("┐(ﾟ ～ﾟ )┌")
            
        @bot.command()
        async def hi(ctx):
            await ctx.message.delete()
            await ctx.send("( ^_^)／")
            
        @bot.command()
        async def ipup(ctx,ip):    
            await ctx.message.delete()
            jsonrequest = requests.get(f'https://ipinfo.io/{ip}/json')
            if "Wrong ip" in jsonrequest.text:
                await ctx.send("Invalid IP address")
                return
            else:
                pass
                json = jsonrequest.json()
                try:
                    ipinfout = f'***Ip info for***`{ip}` \nCity = ***{json["city"]}***\nRegion = ***{json["region"]}***\ncountry = ***{json["country"]}***\nlocation = ***{json["loc"]}***\nZip = ***{json["loc"]}***\nTimeZone = ***{json["timezone"]}***\nOrganisation = ***{json["org"]}***'
                    await ctx.send(ipinfout)
                except:
                    pass
        
        @bot.command()
        async def spam(ctx,msg,amount):
            await ctx.message.delete()
            coroutforspamming = [ctx.send(msg)for i in range(int(amount))]
            await asyncio.gather(*coroutforspamming)
        
        @bot.command()
        async def pfp(ctx, user: discord.User=None):
            ctx.message.delete()
            if user is None:
                pass
            else:
                try:
                    message= f"[***{user.name}***'s Avatar]\n*{user.avatar_url}*"
                    
                    
                    await ctx.send(message)
                except:    
                    pass

        @bot.command()
        async def purge(ctx,amount:int):
            try:
                await asyncio.sleep(1)
                succes = 0
                
                await ctx.send(f'***starting deletion of `{amount}` message(s)***')
                await asyncio.sleep(5)
                async for message in ctx.message.channel.history(limit=amount):
                    if message.author == bot.user:
                        succes += 1
                        await message.delete()
                    else:
                        pass
                asd = await ctx.send(f'***Deleted `{succes}` message(s)***\n*deleting this message in 10 seconds...*')
                await asyncio.sleep(10)
                await asd.delete()
            except:pass

        #<---starting the bot--->
        try:
            sys.stdout = DEVNULL
            sys.stderr = DEVNULL
            bot.run(tokywoky, bot=False)
        except Exception as e:
            q.put('stopped')
    
    def botinfo():
        util.cls()
        print(Fore.CYAN+"<----------Commands---------->")
        print(Fore.BLUE+"Prefix = §")
        print(Fore.LIGHTBLUE_EX+'"shrug" - returns the ¯\_(ツ)_/¯ emoji')
        print(Fore.LIGHTBLUE_EX+'"disapprove" - returns the ᇂ_ᇂ emoji')
        print(Fore.LIGHTBLUE_EX+'"fu" - returns the ( ͡° ͜つ ͡°)╭∩╮ emoji')
        print(Fore.LIGHTBLUE_EX+'"confused" - returns the ┐(ﾟ ～ﾟ )┌ emoji')
        print(Fore.LIGHTBLUE_EX+'"hi" - returns the ( ^_^)／ emoji')
        print(Fore.LIGHTBLUE_EX+'"spam" - usage: spam <message> <times to spam> , spams a given message (ex: spam "hello" 20)')
        print(Fore.LIGHTBLUE_EX+'"ipup" - usage : ipup <ip>, returns info in chat about an ip (ex: ipup 1.1.1.1)')
        print(Fore.LIGHTBLUE_EX+'"pfp" - usage : pfp <@user>, returns profile pic of a user (ex: pfp @CodeSyncio#7302)')
        print(Fore.LIGHTBLUE_EX+'"purge" - usage : purge <purge amount>, deletes a given amount of msges (ex: purge 100)')
        print(Fore.MAGENTA+"press enter to return to main menu")
        ghinput = input()
        init.MainScreen()

#<----------START----------> 
if __name__ == '__main__':
    global q
    q = Queue()
    
    init.CheckValidy()