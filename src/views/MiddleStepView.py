import tkinter as tk

class TweetsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        header = tk.Label(self, text="This is step 2", bd=2, relief="groove")
        header.pack(side="top", fill="x")