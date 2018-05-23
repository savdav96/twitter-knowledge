from tkinter import ttk
import tkinter as tk
#from src.views.App import App


class SubmissionView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        text = tk.Label(self, text=" Welcome to the Twitter Knowledge detector! \n\n"
                                     "To begin with, please enter a search query \n"
                                     "and then press SUBMIT button.", bd=2, relief="groove")
        submit = ttk.Button(self, text="SUBMIT", command=self.submit_controller)

        entry = ttk.Entry(self)
        text.grid(pady=5, padx=5, columnspan=1, sticky="W"+"E")
        entry.grid(row=1, column=0, sticky="W"+"E", padx=5)
        #submit.grid(row=1, column=1, sticky="E", padx=5)


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

            self.tweets = self.twitter.search_no_stream(q=query, pretty=self.pretty.get(), num=30)
            self.tweets = cleaner(self.tweets)
            self.status.configure(text="Results printed below")
            print("#############################################################################")
            for tweet in self.tweets:
                print(tweet)

        if len(self.tweets):

            self.tokenize.configure(state="normal")

        print("\n")

        return