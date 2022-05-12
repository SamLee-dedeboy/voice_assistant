import play_yt

def execute_command(sentence):
    if 'alexa' not in sentence:
        return False, sentence
    play_yt.play("Best of SteinsGate OST  Relaxing Anime BGM For Sleeping or Studying.3gpp")
    return True, sentence

