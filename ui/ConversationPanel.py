import customtkinter
from MessageFrame import messageFrame


class conversationPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=550, height=500, label_text="CHAT BOT")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._next_row = 0

    def create_message_frame(self, message, sender):
        new_message_frame = messageFrame(self, message, sender)
        new_message_frame.grid(row=self._next_row,
                               column=0,
                               padx=2,
                               pady=5,
                               sticky="ew")
        self._next_row += 1
