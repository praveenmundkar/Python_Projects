from pygame import mixer
from time import time ,sleep
from datetime import datetime


init_water = time()
init_eye = time()
init_phyex = time()

watertime = 25*60
eyestime = 30*60
phytime = 45*60


def musicloop(file,stopper) :
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a = int(input("press 1 for Done\n"
                  "      2 for remind me in 5 min"))
    if a == stopper :
        mixer.music.stop()

    elif a == 2:
        mixer.music.stop()
        sleep(300)
    else:
        musicloop(file,stopper)

def log(k):
    with open("logs.txt","a") as f :
        f.write(f" {k} at { datetime.now()}" )

if __name__ == '__main__':

    while True:
        if time()-init_water >watertime :
            musicloop("Water.wav",1)
            init_water=time()
            log("Drank Water")

        if time()-init_eye >eyestime:
            musicloop("eyes.wav",1)
            init_eye=time()
            log("Eyes Relaxation Done")

        if time()-init_phyex >phytime:
            musicloop("Physical.wav",1)
            init_phyex=time()
            log("Physical Exercise Done")
