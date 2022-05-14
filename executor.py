from msilib.schema import Media
from time import time


from difflib import SequenceMatcher

import os
from mediaplayer import MediaPlayer


class Executor:
    def __init__(self):
        self.media_player = MediaPlayer()
    def execute_command(self, sentence):
        if 'alexa' not in sentence:
            return False, sentence
        sentence = sentence.replace("alexa", "").strip()

        if 'play' in sentence:
            target = self.extract_play_target(sentence)
            self.media_player.play(target)
        if 'stop' in sentence:
            self.media_player.stop()

        if 'open' in sentence:
            #target = open_manager.extract_target(sentence)
            target = "taskmgr"
            os.system(target)

        return True, sentence

    def extract_play_target(self, sentence):
        play_list = self.media_player.get_play_list()
        target = sentence.replace("play", "").strip()
        
        similarity_list = list(map(lambda candidate: similarity_score(candidate, target), play_list))
        most_similar_index = similarity_list.index(max(similarity_list))

        winner_name = play_list[most_similar_index]

        return winner_name
def similarity_score(a, b):
    return SequenceMatcher(None, a, b).ratio()

