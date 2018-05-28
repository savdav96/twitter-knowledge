from tkinter import ttk
import tkinter as tk
from src.models.twitter.TwitterClient import TwitterClient


class StartView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.tweets = []
        self.model = TwitterClient()

        text = tk.Label(self, text=" Welcome to the Twitter Knowledge detector! \n\n"
                                     "To begin with, please enter a search query, \n"
                                     "specify the amount of tweets "
                                     "and press SUBMIT.", bd=2, relief="groove")

        self.entry = ttk.Entry(self)
        self.spinbox = Spinbox(self, from_=0, to=100, width=10)
        text.pack(pady=5, padx=5, fill="both", side="top", expand=True)
        self.spinbox.pack(side="right", fill="y", padx=5, pady=5)
        self.entry.pack(fill="x", side="left", expand=True, padx=5, pady=5)


class Spinbox(ttk.Widget):
    def __init__(self, master, **kw):
        ttk.Widget.__init__(self, master, 'ttk::spinbox', kw)

    def get(self):
        return self.tk.call(self._w, 'get')
