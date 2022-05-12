import vlc
import time 
from pytube import YouTube
import random
steins_gate_player = [0, 125, 283, 365, 457, 710, 838, 919, 1170, 1323]
def play(url):
    #YouTube(url).streams.first().download()

    #video = pafy.new(url)
    #best = video.getbest()
    #media = vlc.MediaPlayer(best.url)

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()
    Media.add_option('start-time='+str(random.choice(steins_gate_player)))

    player.set_media(Media)
    player.play()
    time.sleep(10)
    while player.is_playing():
        time.sleep(1)

def download(url):
    YouTube(url).streams.first().download()

