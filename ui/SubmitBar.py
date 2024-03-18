import customtkinter
import sys
sys.path.append('../text_ai')
sys.path.append('../voice_ai')
from TextAi import textAi
from tts import textToSpeech
from stt import speechToText
from AudioRecorder import audioRecorder


class submitBar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=500, height=125)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ai = textAi()
        self.tts = textToSpeech()
        self.conversation_panel = None

        self.prompt_entry = customtkinter.CTkEntry(self,
                                                   width=400,
                                                   placeholder_text="Message The Chat Bot")
        self.prompt_entry.grid(row=0, column=0, padx=5, pady=5)
        self.prompt_text = ""

        self.send_message_button = customtkinter.CTkButton(self,
                                                           text="send_message",
                                                           border_width=2,
                                                           width=50,
                                                           command=self.sendMessageButtonCallBack)
        self.send_message_button.grid(row=0, column=2, padx=5)

        self.activate_microphone_button = customtkinter.CTkButton(self,
                                                                  text="mic",
                                                                  border_width=2,
                                                                  width=50,
                                                                  command=self.activateMicrophoneButtonCallBack)
        self.activate_microphone_button.grid(row=0, column=1, padx=5)

    def set_conversation_panel(self, conversation_panel):
        self.conversation_panel = conversation_panel

    def sendMessageButtonCallBack(self):
        self.prompt_text = self.prompt_entry.get()
        print(self.prompt_text)
        self.prompt_entry.delete(0, "end")

        if self.conversation_panel and len(self.prompt_text) > 0:
            self.conversation_panel.create_message_frame(self.prompt_text,
                                                         "User")
            self.prompt_text = self.ai.response(self.prompt_text)
            self.conversation_panel.create_message_frame(self.prompt_text,
                                                         self.ai.model)
            self.tts.convert_to_speech(self.prompt_text)

    def activateMicrophoneButtonCallBack(self):
        print("mic activated")
        audio = audioRecorder()
        audio.start_recording()
        audio.save_to_file()
        audio.stop_recording()
        speech = speechToText()
        text = speech.convert_audio("recorded_audio.wav")
        if self.conversation_panel and len(text) > 0:
            self.conversation_panel.create_message_frame(text,
                                                         "User")
            self.prompt_text = self.ai.response(text)
            self.conversation_panel.create_message_frame(self.prompt_text,
                                                         self.ai.model)
            self.tts.convert_to_speech(self.prompt_text)
