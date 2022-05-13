from logging.config import listen
import speech_recognition as sr
import pyttsx3
from executor import Executor
import threading

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
                    #res, response = threading.Thread(target=executor.execute_command, args=(command,))
                    t = threading.Thread(target=executor.execute_command, args=(command,))
                    t.start()
                    # if res:
                    #     voice_engine.say(response)
                    #     voice_engine.runAndWait()
                except:
                    pass
        # except:
        #         pass
if __name__ == "__main__":
    main()