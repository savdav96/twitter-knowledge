import tkinter as tk
from tkinter import ttk


class IMBResponseView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        text = tk.Label(self, text=" Here is shown the IBM Watson Response \n"
                                   " in terms of confidency", bd=2, relief="groove", justify="left")

        self.entry = ttk.Entry(self)
        text.grid(pady=5, padx=5, columnspan=1, sticky="W" + "E")
        self.entry.grid(row=1, column=0, sticky="W" + "E", padx=5)