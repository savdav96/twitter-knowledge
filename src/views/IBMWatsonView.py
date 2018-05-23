import tkinter as tk

class IMBResponseView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        header = tk.Label(self, text="This is step 3", bd=2, relief="groove")
        h2 = tk.Label(self, text="This is step 3", bd=2, relief="groove")
        h3 = tk.Label(self, text="This is step 3", bd=2, relief="groove")

        header.pack(side="top", fill="x")
        h2.pack(side="top", fill="x")
        h3.pack(side="top", fill="x")