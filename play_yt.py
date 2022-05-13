import vlc
import time 
from pytube import YouTube
import random
steins_gate_player = [0, 125, 283, 365, 457, 710, 838, 919, 1170, 1323]
stop_flag = False
class Yt_Player:
    def __init__(self):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.stop_flag = False
        self.now_playing = ""
    def play(self, url, start_time):
        #YouTube(url).streams.first().download()

        #video = pafy.new(url)
        #best = video.getbest()
        #media = vlc.MediaPlayer(best.url)

        
        Media = self.Instance.media_new(url)
        Media.get_mrl()
        Media.add_option('start-time='+start_time)
        self.player.set_media(Media)
        self.player.play()
        self.now_playing = url.split(".")[0]
        time.sleep(10)
        while self.player.is_playing() and self.stop_flag!=True:
            time.sleep(1)

    def stop(self):
        #self.stop_flag = True
        self.player.stop()


def download(url):
    YouTube(url).streams.first().download()

