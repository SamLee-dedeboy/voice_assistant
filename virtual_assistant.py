from logging.config import listen
import speech_recognition as sr
import pyttsx3
from executor import Executor

def main():
        listener = sr.Recognizer()
        voice_engine = pyttsx3.init()
        executor = Executor()
        # try:
        with sr.Microphone() as source:
            while(True):
                try:
                    print("--> adjusting ambient noise...", end='', flush=True)
                    listener.adjust_for_ambient_noise(source, duration = 5)
                    print("done.")
                    print("--> listenting...")
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice).lower()
                    print(command)
                    res, response = executor.execute_command(command)
                    if res:
                        print(response)
                        #voice_engine.say(response)
                        #voice_engine.runAndWait()
                except:
                    pass
        # except:
        #         pass
if __name__ == "__main__":
    main()