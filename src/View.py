from tkinter import ttk
import tkinter as tk
from src.TwitterClient import *
from src.Tokenizer import *
from src.WitAI_Gwent import WitAi

class View:

    def __init__(self, master):

        self.pretty = tk.BooleanVar()
        self.stream = tk.BooleanVar()
        self.tweets = []
        self.tokens = []
        self.twitter = TwitterClient()
        self.witai = WitAi
        self.frame = tk.Frame(master)
        self.create_widget()

    def create_widget(self):

        # Creates widgets and packs them into the Tk() frame

        self.stop = ttk.Button(text="STOP", command=self.stop_controller)
        self.submit = ttk.Button(text="Submit", command=self.submit_controller)
        self.witai = ttk.Button(text="Ask wit.ai", command=self.witai_controller)
        self.tokenize = ttk.Button(text="Tokenize", state="disabled", command=self.tokenize_controller)
        self.text = ttk.Label(text="Input the search query/stream filter:")
        self.entry = ttk.Entry()
        self.use_pretty = ttk.Checkbutton(text="Pretty Print", variable=self.pretty)
        self.use_stream = ttk.Checkbutton(text="Stream (BETA)", variable=self.stream)
        self.status = ttk.Label(text="Ready")
        self.packer()

    def packer(self):

        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry.grid(row=0, column=2, ipadx=100, pady=5, padx=5)
        self.use_pretty.grid(row=0, column=3)
        self.use_stream.grid(row=0, column=4)
        self.submit.grid(row=0, column=6, padx=5, pady=5)
        self.witai.grid(row=1, column=6, padx=5, pady=5)
        self.status.grid(row=1, column=1)
        self.tokenize.grid(row=1, column=5)

        return

    def tokenize_controller(self):

        # Calls tokenize function from Tokenizer.py

        self.tokens = get_tokens(self.tweets)
        self.status.configure(text="Tweets tokenized")
        print(len(self.tokens))

        return

    def witai_controller(self):

        self.witai.wit_ai_request(q=self.tweets["text"])
        print(self.witai.get_response())


    def submit_controller(self):

        # Either runs a Twitter stream or searches a finite set of results, depending on "stream" flag

        self.stop.grid_forget()
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

            self.tweets = self.twitter.search_no_stream(q=query, pretty=self.pretty.get(), num=100)
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

    # Defines the frame application

    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run(self):
        self.root.title("Twitter Knowledge")
        self.root.resizable(False, False)
        self.root.deiconify()
        self.root.mainloop()

