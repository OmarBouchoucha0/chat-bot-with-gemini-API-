import customtkinter


class messageFrame(customtkinter.CTkFrame):
    def __init__(self, master, message, sender):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        self.message = message
        self.sender = sender
        self.sender_label = customtkinter.CTkLabel(self,
                                                   text=self.sender,
                                                   fg_color="transparent")
        self.sender_label.grid(row=0, column=0)

        self.textbox = customtkinter.CTkTextbox(self,
                                                corner_radius=5,
                                                height=200,
                                                state="disabled",
                                                wrap="word")
        self.textbox.grid(row=1, column=0, sticky="ew")
        self.textbox.configure(state="normal")
        self.textbox.insert("0.0", self.message)
        self.textbox.configure(state="disabled")
