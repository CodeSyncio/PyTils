import __main__
from colorama import Fore
from subprocess import DEVNULL,STDOUT
from ctypes import *

def cls():
    __main__.util.cls()
def mainscrn():
    __main__.init.MainScreen()
    
def InstantBSOD():
        cls()
        print(Fore.LIGHTRED_EX+"WARNING: this will INSTANTLY crash your system! only use this for testing! continue? [y/n]")
        bsodinput = input()
        if bsodinput == "y":
            print(Fore.LIGHTRED_EX+"CRASHING...")
            from ctypes import windll
            from ctypes import c_int
            from ctypes import c_uint
            from ctypes import c_ulong
            from ctypes import POINTER
            from ctypes import byref
            nullptr = POINTER(c_int)()
            windll.ntdll.RtlAdjustPrivilege(c_uint(19) , c_uint(1) , c_uint(0) , byref(c_int()))
            windll.ntdll.NtRaiseHardError(c_ulong(0xC000007B) , c_ulong(0) , nullptr , nullptr , c_uint(6) , byref(c_uint()))
        else:
            mainscrn()
    