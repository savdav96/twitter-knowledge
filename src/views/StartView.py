from tkinter import ttk
import tkinter as tk
from src.models.twitter.TwitterClient import TwitterClient


class StartView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.tweets = []
        self.model = TwitterClient()

        text = tk.Label(self, text=" Welcome to the Twitter Knowledge detector! \n\n"
                                     "To begin with, please enter a search query \n"
                                     "and then press SUBMIT button.", bd=2, relief="groove")

        self.entry = ttk.Entry(self)
        self.entry.pack(fill="x", side="bottom", expand=True, padx=5)
        text.pack(pady=5, padx=5, fill="both", side="top", expand=True)




