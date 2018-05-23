from tkinter import ttk
import tkinter as tk
import datetime
from src.models.twitter.TwitterClient import *
from deprecated.WitAIClient import *


class View:

    def __init__(self, master):

        self.pretty = tk.BooleanVar()
        self.stream = tk.BooleanVar()
        self.tweets = []
        self.tokens = []
        self.twitter = TwitterClient()
        self.witai = WitAIClient
        self.IBMWatson = IBMWatsonClient()
        self.statistics = DataMiningStatistics()
        self.positive = False
        self.true = False
        self.data = load_obj("twitter knowledge data")
        if self.tweets.__len__() > 0:
            self.current_tweet = self.tweets[0]
        else:
            self.current_tweet = "..."
        self.relations = []
        self.frame = tk.Frame(master)
        self.create_widget()


    def create_widget(self):

        # Creates widgets and packs them into the Tk() frame
        self.emptyRow = ttk.Label()
        self.stop = ttk.Button(text="STOP", command=self.stop_controller)
        self.submit = ttk.Button(text="Submit", command=self.submit_controller)
        self.IBMWatsonButton = ttk.Button(text="Ask IBMWatson", command=self.IBMWatson_controller)
        self.tokenize = ttk.Button(text="Tokenize", state="disabled", command=self.tokenize_controller)
        self.text = ttk.Label(text="Input the search query/stream filter:")
        self.entry = ttk.Entry()
        self.use_pretty = ttk.Checkbutton(text="Pretty Print", variable=self.pretty)
        self.use_stream = ttk.Checkbutton(text="Stream (BETA)", variable=self.stream)
        self.recognized = ttk.Label(text="Tweet recognized?")
        self.recognizedY = ttk.Button(text="Yes", state="disabled", command=self.set_positive)
        self.recognizedN = ttk.Button(text="No", state="disabled", command=self.set_negative)
        self.knownIntent = ttk.Label(text="Known intent?")
        self.knownIntentY = ttk.Button(text="Yes", state="disabled", command=self.set_true)
        self.knownIntentN = ttk.Button(text="No", state="disabled", command=self.precision_recall)
        self.save = ttk.Button(text="Save", command=self.save_data)
        self.show_data = ttk.Button(text="Show Data", command=self.print_data)
        self.current_tweet_label=ttk.Label(text="Last tweet:\t" + self.current_tweet)
        self.status = ttk.Label(text="Ready")
        self.packer()

    def packer(self):

        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry.grid(row=0, column=2, ipadx=100, pady=5, padx=5)
        self.use_pretty.grid(row=0, column=3)
        self.use_stream.grid(row=0, column=4)
        self.submit.grid(row=0, column=6, padx=5, pady=5)
        self.IBMWatsonButton.grid(row=1, column=6, padx=5, pady=5)
        self.emptyRow.grid(row=4, column=1)
        self.status.grid(row=5, column=1)
        self.tokenize.grid(row=1, column=5)
        self.recognized.grid(row=2, column=1)
        self.knownIntent.grid(row=3, column=1)
        self.recognizedY.grid(row=2, column=2)
        self.recognizedN.grid(row=2, column=3)
        self.knownIntentY.grid(row=3, column=2)
        self.knownIntentN.grid(row=3, column=3)
        self.current_tweet_label.grid(columnspan=4, row=4, column=1)
        self.save.grid(row=4, column=6)
        self.show_data.grid(row=4, column=5)

        return

    def tokenize_controller(self):

        # Calls tokenize function from TokenizerUtils.py

        self.tokens = get_tokens(self.tweets)
        self.status.configure(text="Tweets tokenized")
        print(len(self.tokens))

        return

    def witai_controller(self):
        for tweet in self.tweets:
            self.witai.wit_ai_request(q=tweet)
            print(self.witai.get_response())

    def IBMWatson_controller(self):

        if self.tweets.__len__() > 0:
            self.IBMWatson.watson_request(q=self.tweets[0]["text"])
            response = self.IBMWatson.get_response()
            print("\nWatson Assistant response:")
            print(response['intents'])
            print(response['entities'])
            relation = {'Relation': response['intents'],
                        'Entities involved': response['entities'],
                        'Tweet text': self.tweets[0]["text"]}
            self.relations.append(relation)
            self.recognizedY.configure(state="normal")
            self.recognizedN.configure(state="normal")
            self.update_current_tweet()
            self.tweets.remove(self.tweets[0])

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

    def stop_controller(self):

        # Stops the Twitter stream

        self.status.configure(text="Stopped. Check <tweets.json>")
        self.twitter.stop_stream()

        return

    def set_positive(self):
        self.positive = True
        self.recognizedY.configure(state="disabled")
        self.recognizedN.configure(state="disabled")
        self.knownIntentY.configure(state="normal")
        self.knownIntentN.configure(state="normal")

    def set_negative(self):
        self.recognizedY.configure(state="disabled")
        self.recognizedN.configure(state="disabled")
        self.knownIntentY.configure(state="normal")
        self.knownIntentN.configure(state="normal")

    def set_true(self):
        self.true = True
        self.precision_recall()

    def precision_recall(self):
        if self.positive & self.true:
            self.statistics.TP = +1
        if self.positive & (not self.true):
            self.statistics.NP = +1
        if (not self.positive) & self.true:
            self.statistics.TN = +1
        if (not self.positive) & (not self.true):
            self.statistics.FN = +1
        self.positive = False
        self.true = False
        self.knownIntentY.configure(state="disabled")
        self.knownIntentN.configure(state="disabled")

    def save_data(self):
        self.data.append({'Date': str(datetime.datetime.now()),
                          'Precision': self.statistics.get_precision,
                          'Recall': self.statistics.get_recall,
                          'Amount of analyzed tweets': self.statistics.sample_dimension,
                          'Relations': self.relations})
        save_obj(self.data, "twitter knowledge data")

    def print_data(self):
        print(self.data)

    def update_current_tweet(self):
        if self.tweets.__len__() > 0:
            self.current_tweet = self.tweets[0]
        else:
            self.current_tweet = "..."
        self.current_tweet_label.configure(text="Last tweet:\t" + self.current_tweet['text'])


class App:

    # Defines the frame application

    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run(self):
        self.root.title("Twitter Knowledge")
        self.root.resizable(True, True)
        self.root.deiconify()
        self.root.mainloop()

