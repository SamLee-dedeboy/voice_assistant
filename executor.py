from time import time
import play_yt


from difflib import SequenceMatcher
import json
from play_yt import Yt_Player
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
            return random.choice(timestamp)
        if format == 'min_secs':
            return random.choice(list(map(min_sec_to_sec, timestamp)))
        

class Executor:
    def __init__(self):
        self.play_list_manager = Play_list("play_list.json")
        self.play_list = self.play_list_manager.get_play_list()
        self.player = Yt_Player()
    def execute_command(self, sentence):
        if 'alexa' not in sentence:
            return False, sentence
        sentence = sentence.replace("alexa", "").strip()
        if 'play' in sentence:
            (start, url) = self.extract_play_target(sentence)
            self.player.play(url, start)
        if 'stop' in sentence:
            self.player.stop()
        return True, sentence

    def extract_play_target(self, sentence):
        target = sentence.replace("play", "").strip()
        
        similarity_list = list(map(lambda candidate: similarity_score(candidate, target), self.play_list))
        most_similar_index = similarity_list.index(max(similarity_list))

        winner_name = self.play_list[most_similar_index]
        return (self.play_list_manager.get_random_start(winner_name), self.play_list_manager.get_url_by_name(winner_name))
def similarity_score(a, b):
    return SequenceMatcher(None, a, b).ratio()
def min_sec_to_sec(min_sec):
    return str(int(min_sec.split(":")[0])*60 + int(min_sec.split(":")[1]))
