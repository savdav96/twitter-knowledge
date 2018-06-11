import pprint
from tkinter import ttk, messagebox
import tkinter as tk
import datetime

from models.utils.DataMiningUtils import DataMiningStatistics
from models.utils.IOUtils import save_obj, load_obj
from src.controllers.TwitterController import TwitterController
from src.controllers.IBMWatsonController import IBMWatsonController
from src.views.StartView import StartView
from src.views.TweetsView import TweetsView
from src.views.IBMWatsonView import IMBResponseView


class AppView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.cleaned_tweets = []
        self.current_step = None
        self.statistics = DataMiningStatistics()
        self.data = load_obj("twitter knowledge data")
        self.relations = []

        self.steps = [StartView(self), TweetsView(self)]

        self.button_frame = tk.Frame(self, bd=1, relief="raised")
        self.content_frame = tk.Frame(self)

        self.back_button = ttk.Button(self.button_frame, text="< Back", command=self.back_button)
        self.save_button = ttk.Button(self.button_frame, text="Save", command=self.save_controller)
        self.print_data_button = ttk.Button(self.button_frame, text="Print data", command=self.print_data_controller)
        self.print_FP_FN_button = ttk.Button(self.button_frame, text="Print FP/FN", command=self.print_FP_FN)
        self.submit_button = ttk.Button(self.button_frame, text="Submit >", command=self.submit)
        self.close_button = ttk.Button(self.button_frame, text="Quit", command=self.quit)
        self.ibm_watson_button = ttk.Button(self.button_frame, text="Ask IBMWatson >", command=self.ibm_watson_controller)

        self.button_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        self.content_frame.pack(side="top", fill="both", anchor="n")

        self.show_step(0)

    def show_step(self, step):

        if self.current_step is not None:
            # remove current step
            current_step = self.steps[self.current_step]
            current_step.pack_forget()

        self.current_step = step

        new_step = self.steps[step]
        new_step.pack(side="top", fill="both", expand=True)

        if step == 0:
            self.submit_button.pack(side="right")
            self.close_button.pack(side="left")
            self.back_button.pack_forget()
            self.save_button.pack_forget()
            self.print_data_button.pack_forget()
            self.ibm_watson_button.pack_forget()
            self.print_FP_FN_button.pack_forget()

        else:
            self.back_button.pack(side="left")
            self.ibm_watson_button.pack(side="right")
            self.save_button.pack(side="left")
            self.print_data_button.pack(side="left")
            self.print_FP_FN_button.pack(side="left")
            self.close_button.pack_forget()
            self.submit_button.pack_forget()

    def next(self):
        self.show_step(self.current_step + 1)

    def back(self):
        self.show_step(self.current_step - 1)

    def back_button(self):
        self.steps[1].listbox.delete(0, "end")
        self.back()

    def print_data_controller(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.data)

    def print_FP_FN(self):
        k = 0
        for i in self.data:
            k += 1
            for j in i['Relations']:
                if k < 2:               # first two elements of dictionary hasn't the field "Test result"
                    break
                if j['Test result'] == "FP" or j['Test result'] == "FN":
                    print(j['Tweet text'])

    def save_controller(self):
        self.data.append({'Date': str(datetime.datetime.now()),
                          'Precision': float(self.statistics.get_precision()),
                          'Recall': float(self.statistics.get_recall()),
                          'Amount of analyzed tweets': self.statistics.sample_dimension,
                          'Relations': self.relations})
        save_obj(self.data, "twitter knowledge data")

    def submit(self):
        self.submit_controller()
        self.next()

    def ibm_watson(self):
        self.ibm_watson_controller()
        self.next()

    def ibm_watson_controller(self):
        id = None
        query = self.steps[1].listbox.get("active")
        for i in self.cleaned_tweets:
            if query == i['text']:
                id = i['id']
                break
        controller = IBMWatsonController()
        controller.ask_ibm_watson(query, id)
        controller.print_response()
        root = tk.Tk()
        IMBResponseView(root, controller.get_response(), self.statistics, controller.get_last_relation_found(),
                        self.relations).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def submit_controller(self):

        query = self.steps[0].entry.get()
        listbox = self.steps[1].listbox
        self.steps[0].spinbox.get()
        controller = TwitterController()
        if not query:
            messagebox.showwarning("Warning", "Input field must not be empty!")
            return
        if not self.steps[0].spinbox.get():
            messagebox.showwarning("Warning", "Number of tweets field must not be empty!")
            return

        print("You wrote: " + query + "\n")

        controller.search(q=query, num=self.steps[0].spinbox.get())

        self.cleaned_tweets = controller.get_cleaned_tweets()
        controller.save_raw_tweets()
        for tweet in self.cleaned_tweets:
            listbox.insert("end", tweet['text'])

