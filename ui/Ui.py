import customtkinter
from SubmitBar import submitBar
from ConversationPanel import conversationPanel


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.geometry("600x600")
        customtkinter.set_default_color_theme("dark-blue")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)
        self.conversation_panel = conversationPanel(self)
        self.conversation_panel.grid(row=0,
                                     column=0,
                                     padx=10,
                                     pady=2)
        self.submit_bar = submitBar(self)
        self.submit_bar.grid(row=1,
                             column=0,
                             padx=10,
                             pady=2)
        self.submit_bar.set_conversation_panel(self.conversation_panel)


if __name__ == "__main__":
    app = App()
    app.title("Chat Bot")
    app.mainloop()
