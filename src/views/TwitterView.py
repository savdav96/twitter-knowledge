from tkinter import ttk
import tkinter as tk
from src.models.twitter.TwitterClient import TwitterClient


class TwitterView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.tweets = []
        self.model = TwitterClient()

        text = tk.Label(self, text=" Welcome to the Twitter Knowledge detector! \n\n"
                                     "To begin with, please enter a search query \n"
                                     "and then press SUBMIT button.", bd=2, relief="groove")

        self.entry = ttk.Entry(self)
        text.grid(pady=5, padx=5, columnspan=1, sticky="W"+"E")
        self.entry.grid(row=1, column=0, sticky="W"+"E", padx=5)



