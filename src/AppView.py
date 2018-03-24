from tkinter import ttk
import tkinter as tk
from src.TwitterClient import *


class AppView:

    def __init__(self, master):

        self.pretty = tk.BooleanVar()
        self.stream = tk.BooleanVar()
        self.tweets = []
        self.twitter = TwitterClient()
        self.frame = tk.Frame(master)
        self.create_widget()

    def create_widget(self):

        # Creates widgets and packs them into the Tk() frame

        self.stop = ttk.Button(text="STOP", command=self.stop_controller, state="disabled")
        self.submit = ttk.Button(text="Submit", command=self.submit_controller)
        self.tokenize = ttk.Button(text="Tokenize", state="disabled")
        self.text = ttk.Label(text="Input the search query:", font=("Helvetica", 10))
        self.entry = ttk.Entry()
        self.usePretty = ttk.Checkbutton(text="Pretty Print", variable=self.pretty)
        self.useStream = ttk.Checkbutton(text="Stream", variable=self.stream)
        self.status = ttk.Label(text="Ready")
        self.packer()

    def packer(self):

        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry.grid(row=0, column=2)
        self.usePretty.grid(row=0, column=3)
        self.useStream.grid(row=0, column=5)
        self.stop.grid(row=0, column=6)
        self.submit.grid(row=0, column=7, padx=5, pady=5)
        self.tokenize.grid(row=1, column=7, padx=5, pady=5)
        self.status.grid(row=1, column=1)

        return

    def tokenize_controller(self):

        print(len(self.tweets))

        return

    def submit_controller(self):

        # Starts a Twitter stream from TwitterClient attribute

        query = self.entry.get()
        print("You wrote: " + query)

        if not self.stream:
            self.tweets = self.twitter.search_no_stream(q=query, pretty=self.pretty.get(), num=5)
        else:
            self.twitter.start_stream(q=query)
            self.stop.configure(state="normal")
        self.tokenize.configure(state="normal")

        return

    def stop_controller(self):

        # Stops the Twitter stream
        self.twitter.stop_stream()


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.view = AppView(self.root)

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.resizable(False, False)
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.quit()
