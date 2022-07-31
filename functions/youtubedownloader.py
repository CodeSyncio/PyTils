import __main__
from colorama import Fore
import os ,sys
from pytube import YouTube
def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def ytdownloader():
        if os.path.exists('youtube-downloads'):
            pass
        else:
                    
            os.mkdir('youtube-downloads')
        cls()
        
        def on_progresscheck(stream, chunk: bytes, bytes_remaining: int):
            current = ((stream.filesize - bytes_remaining)/stream.filesize)
            progress = int(50*current)
            status = '█' * progress + '-' * (50 - progress)
            
            sys.stdout.write(Fore.LIGHTCYAN_EX+f'--> |{status}| {round(current*100)} %\r')
            sys.stdout.flush()
            
        print(Fore.CYAN+"Please enter the yt link:")
        
        link = input()
        if link=='':
            mainscrn()
        yt = YouTube(link,on_progress_callback=on_progresscheck)
        vt = yt.title
        ys = yt.streams.get_highest_resolution()
        size = round(ys.filesize/1000000)
        cls()
        print(Fore.MAGENTA+f"Starting download of video [{vt}]  ({size} MB)")
        ys.download(output_path=f'{os.getcwd()}/youtube-downloads/')
        print(Fore.GREEN+f"\nSucessfully downloaded {vt}, file is saved in the 'youtube-downloads' folder")
        
        print(Fore.MAGENTA+"\nPress enter to return to the main menu ,any other key to download another video")
        ghinput = input()
        if ghinput =='':
            mainscrn()
        else:
            ytdownloader()