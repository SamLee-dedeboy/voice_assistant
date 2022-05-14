from play_yt import Yt_Player
import json
import random

class Play_list:
    def __init__(self, play_list_data):
        self.play_list_data = json.load(open(play_list_data))["play_list"]
        self.play_list_dict = {}
        for item in self.play_list_data:
            self.play_list_dict[item["name"]] = item
    def get_play_list(self):
        return list(map(lambda x: x["name"], self.play_list_data))
    
    def get_url_by_name(self, name):
        return self.play_list_dict[name]['url']
    def get_random_start(self, name):
        target = self.play_list_dict[name]
        format = target['format']
        timestamp = target['time_stamp']
        if format == 'seconds':
            return str(random.choice(timestamp))
        if format == 'min_secs':
            return random.choice(list(map(min_sec_to_sec, timestamp)))
        
class MediaPlayer:
    def __init__(self):
        self.play_list_manager = Play_list("play_list.json")
        self.play_list = self.play_list_manager.get_play_list()
        self.player = Yt_Player()
    def play(self, target):
        start = self.play_list_manager.get_random_start(target)
        url = self.play_list_manager.get_url_by_name(target)
        self.player.play(start_time=start, url=url)

    def stop(self):
        self.player.stop()

    def get_play_list(self):
        return self.play_list_manager.get_play_list()
def min_sec_to_sec(min_sec):
    return str(int(min_sec.split(":")[0])*60 + int(min_sec.split(":")[1]))