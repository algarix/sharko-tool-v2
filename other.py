import time 
import os 
def other():
    os.system('cls')
    n = input("do you want open the tool ? (y/n)=  ")
    if n == 'y':
        print("open cmd in the folder and type python tool.py")
        time.sleep(10)
        exit()
    if n == 'n':
        os.system('cls')
        nr()
    else:
        print("mmmh")
        time.sleep(2)
        os.system('cls')
        other()


        
def nr():
    r = input("𝓪𝓻𝒆 𝔂𝓸𝓾𝓻 𝓼𝓾𝓻𝒆 ? (n/y)= ")
    if r == 'y':
        print("mmh")
        time.sleep(2)
        os.system('cls')
        nr()
    if r =='n':
        print("for launch the tool open cmd in the folder and type python tool.py (＾▽＾)")
        time.sleep(10)
    else:
        print("mmh")
        time.sleep(2)
        os.system('cls')
        other()


other()
