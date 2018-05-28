from tkinter import ttk, messagebox
import tkinter as tk

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

        self.steps = [StartView(self), TweetsView(self), IMBResponseView(self)]

        self.button_frame = tk.Frame(self, bd=1, relief="raised")
        self.content_frame = tk.Frame(self)

        self.back_button = ttk.Button(self.button_frame, text="<< Back", command=self.back)
        self.next_button = ttk.Button(self.button_frame, text="Next >>", command=self.next)
        self.finish_button = ttk.Button(self.button_frame, text="Finish", command=self.finish)
        self.submit_button = ttk.Button(self.button_frame, text="Submit >>", command=self.submit)
        self.close_button = ttk.Button(self.button_frame, text="Quit", command=self.quit)
        self.ibm_watson_button = ttk.Button(self.button_frame, text="Ask IBMWatson >>", command=self.ibm_watson_controller)

        self.button_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        self.content_frame.pack(side="top", fill="both", expand=True)

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
            # first step
            self.submit_button.pack(side="right")
            self.close_button.pack(side="left")
            self.back_button.pack_forget()
            self.next_button.pack_forget()
            self.finish_button.pack_forget()
            self.ibm_watson_button.pack_forget()

        elif step == len(self.steps)-1:
            # last step
            self.back_button.pack(side="left")
            self.finish_button.pack(side="right")
            self.next_button.pack_forget()
            self.close_button.pack_forget()
            self.submit_button.pack_forget()
            self.ibm_watson_button.pack_forget()

        else:
            # all other steps
            self.back_button.pack(side="left")
            self.next_button.pack_forget()
            self.ibm_watson_button.pack(side="right")
            self.close_button.pack_forget()
            self.submit_button.pack_forget()
            self.finish_button.pack_forget()

    def next(self):
        self.show_step(self.current_step + 1)

    def back(self):
        self.show_step(self.current_step - 1)

    def finish(self):
        pass

    def submit(self):
        self.submit_controller()
        self.next()

    def ibm_watson(self):
        self.ibm_watson_controller()
        self.next()

    def submit_controller(self):

        query = self.steps[0].entry.get()
        listbox = self.steps[1].listbox

        controller = TwitterController()
        if not query:
            messagebox.showwarning("Warning", "Input must not be empty!")
            return

        print("You wrote: " + query + "\n")

        controller.search(q=query, num=1000)

        self.cleaned_tweets = controller.get_cleaned_tweets()
        for tweet in self.cleaned_tweets:
            listbox.insert("end", tweet)

    def ibm_watson_controller(self):

        query = self.steps[1].listbox.get("active")

        controller = IBMWatsonController()
        controller.ask_ibm_watson(query)
        controller.print_response()

