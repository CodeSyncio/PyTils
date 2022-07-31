import __main__
from colorama import Fore
import os ,sys,requests
from pytube import YouTube
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch
import subprocess
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()

def spotdowload():
        if os.path.exists('spotify-downloads'):
            pass
        else:       
            os.mkdir('spotify-downloads')
        cls()
        
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
                mainscrn()
        print(Fore.CYAN+"Please enter the song link:")
        implink = input()
        if implink=='':
            mainscrn()
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
            mainscrn()
        else:
            spotdowload()     