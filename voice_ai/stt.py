import speech_recognition as sr


class speechToText:
    def __init__(self, language='en-US'):
        self.recognizer = sr.Recognizer()
        self.language = language

    def convert_audio(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data,
                                                        language=self.language)
                return text
            except sr.UnknownValueError:
                print("Sorry, could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Error: {e}")
                return None
