




import time
import speech_recognition as sr
import os

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def list_microphones(self):
        """List available microphones."""
        microphones = sr.Microphone.list_microphone_names()
        return microphones

    def recognize_speech(self):
        """Capture and recognize speech from the microphone."""
        try:
            with sr.Microphone() as source:
                print("Adjusting noise. Please wait...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("You can start speaking now...")

                while True:
                    print("\nListening...")
                    audio = self.recognizer.listen(source, phrase_time_limit=5)
                    try:
                        text = self.recognizer.recognize_google(audio, language="en-US")
                        words = text.split()
                        for word in words:
                            print(word, end=" ", flush=True)
                            time.sleep(0.5)
                    except sr.UnknownValueError:
                        pass  # Ignore unrecognized audio
                    except sr.RequestError as e:
                        print(f"\nCould not request results; {e}")
                        break

        except KeyboardInterrupt:
            print("\nProgram terminated.")

if __name__ == "__main__":
    # Initialize the SpeechRecognizer object
    speech_recognizer = SpeechRecognizer()

    # List available microphones
    print("Available microphones:")
    microphones = speech_recognizer.list_microphones()
    for i, mic in enumerate(microphones):
        print(f"{i}: {mic}")

    # Start speech recognition
    print("\nStarting speech recognition...")
    speech_recognizer.recognize_speech()


