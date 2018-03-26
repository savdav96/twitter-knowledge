from tkinter import ttk
import tkinter as tk
from src.TwitterClient import *
from src.Tokenizer import *


class View:

    def __init__(self, master):

        self.pretty = tk.BooleanVar()
        self.stream = tk.BooleanVar()
        self.tweets = []
        self.twitter = TwitterClient()
        self.frame = tk.Frame(master)
        self.create_widget()

    def create_widget(self):

        # Creates widgets and packs them into the Tk() frame

        self.stop = ttk.Button(text="STOP", command=self.stop_controller)
        self.submit = ttk.Button(text="Submit", command=self.submit_controller)
        self.tokenize = ttk.Button(text="Tokenize", state="disabled", command=self.tokenize_controller)
        self.text = ttk.Label(text="Input the search query/stream filter:")
        self.entry = ttk.Entry()
        self.usePretty = ttk.Checkbutton(text="Pretty Print", variable=self.pretty)
        self.useStream = ttk.Checkbutton(text="Stream (BETA)", variable=self.stream)
        self.status = ttk.Label(text="Ready")
        self.packer()

    def packer(self):

        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry.grid(row=0, column=2)
        self.usePretty.grid(row=0, column=3)
        self.useStream.grid(row=0, column=4)
        self.submit.grid(row=0, column=6, padx=5, pady=5)
        self.tokenize.grid(row=1, column=6, padx=5, pady=5)
        self.status.grid(row=1, column=1)

        return

    def tokenize_controller(self):

        # Calls tokenize function from Tokenizer.py

        get_tokens(self.tweets)
        self.status.configure(text="Tweets tokenized")

        return

    def submit_controller(self):

        # Runs either a Twitter stream or searches a finite set of results, depending on "stream" flag

        query = self.entry.get()

        if not query:

            print("Input must not be empty!")

            return

        print("You wrote: " + query + "\n")

        if self.stream.get():

            self.twitter.start_stream(q=query)
            self.stop.grid(row=0, column=5)
            self.status.configure(text="Streaming in progress...")

        else:

            self.stop.grid_forget()
            self.tweets = self.twitter.search_no_stream(q=query, pretty=self.pretty.get(), num=5)
            self.status.configure(text="Results printed below")

        if len(self.tweets):

            self.tokenize.configure(state="normal")

        print("\n")

        return

    def stop_controller(self):

        # Stops the Twitter stream

        self.status.configure(text="Stopped. Check <tweets.json>")
        self.twitter.stop_stream()

        return


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run(self):
        self.root.title("Twitter Knowledge")
        self.root.resizable(False, False)
        self.root.deiconify()
        self.root.mainloop()

