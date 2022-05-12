from logging.config import listen
import speech_recognition as sr
import pyttsx3
import executor
def main():
        listener = sr.Recognizer()
        voice_engine = pyttsx3.init()
        try:
            with sr.Microphone() as source:
                print("adjusting ambient noise...", end='', flush=True)
                listener.adjust_for_ambient_noise(source, duration = 5)
                print("done.")
                while(True):
                    print("listenting...")
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice).lower()
                    print(command)
                    res, response = executor.execute_command(command)
                    if res:
                        voice_engine.say(response)
                        voice_engine.runAndWait()
        except:
                pass
if __name__ == "__main__":
    main()