from scanner import port_scanner
import sys
import pyfiglet 
from datetime import datetime
import clear
import time
import os



def keys():
    print("\x1b[94;49m")
    os.system('cls')
    ascii_banner = pyfiglet.figlet_format("sharko  tool  V2")
    print(ascii_banner)
    key = input("please enter the key = ") 
    if key == "sharkoV2":
        print("welcome to the V2 version")
        time.sleep(3)
        print("the tool is loaded")
        time.sleep(2)
        os.system('cls')
        paid()
    else:
        print("the keys is incorrect")
        time.sleep(2)
        os.system('cls')
        keys()
def paid():
    from ascii import ascii
    time.sleep(0.5)
    os.system('cls')
    ascii()
    time.sleep(2)
    ascii_banner4 = pyfiglet.figlet_format("sharko tool V2")
    print(ascii_banner4)
    p = input("- 1 network scanner\n- 2 password list generator\n- 3 zip password cracker\n- 4 mailspammer\n- 5 tracker\n- 6 tiktok mass report\n- 7 roblox mass report\n- 8 serveur raider\n- 9 discord tool\n- 10 roblox server grabber\n- 99 credit\n\nplease enter a choice =  ")
    if p == '1':
        os.system('cls')
        ascii_banner3 = pyfiglet.figlet_format("network  scanner")
        print(ascii_banner3)
        port_scanner()
    if p == '2':
        os.system('cls')
        from wordlist import program
    if p =='3':
        os.system('cls')
        ascii3 = pyfiglet.figlet_format("zip cracker")
        print(ascii3)
        from script import script
    if p =='4':
        os.system('cls')
        from mailspammer import main
        main()
    if p == '5':
        os.system('cls')
        from GhostTR import GhostTR
        time.sleep(20)
    if p == '6':
        from tiktok import main
        main()
        print("\x1b[94;49m")
    if p == '7':
        from roblox import roblox
    if p == '8':
        from raider import main 
        main()
    if p == '9':
        from GANG import gang
    if p == '10':
        from server_grabber import server_grabber
        server_grabber()
        time.sleep(10)

    if p == '99':
         print('''this tool was created by me
my discord : algarix
my tiktok : @sharkogtag
if you has idea dm me ! ''')
         os.system('cls')
         paid()
    else:
        print("wrong numbers !")
        time.sleep(1)
        os.system('cls')
        paid()
    



keys()

        
        

        




