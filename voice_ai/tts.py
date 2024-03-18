from gtts import gTTS
import os


class textToSpeech:
    def __init__(self, language='en', region='US', slow=False):
        self.language = language
        self.region = region
        self.slow = slow

    def convert_to_speech(self, text, filename="tts.mp3"):
        tts = gTTS(text=text,
                   lang=self.language,
                   tld=self.region,
                   slow=self.slow)

        tts.save(filename)
        os.system(f"mpg123 {filename}")  # For Linux
