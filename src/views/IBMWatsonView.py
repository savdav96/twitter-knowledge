import tkinter as tk
from tkinter import ttk


class IMBResponseView(tk.Frame):

    def __init__(self, parent, response):
        super().__init__(parent)
        self.response = response

        h1 = tk.Label(self, text=" Here is shown the IBM Watson Response in terms of confidency:", bd=2, relief="groove", justify="center")
        h1.grid(row=0, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        h2 = tk.Label(self, text="Input:", bd=2, relief="groove", justify="center")
        h2.grid(row=1, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        input_query = tk.Label(self, text=self.response["input"]['text'], bd=2, justify="left")
        input_query.grid(row=2, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        h3 = tk.Label(self, text="Intent:", bd=2, relief="groove", justify="center")
        h3.grid(row=3, column=0, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        intents_intent = tk.Label(self, text=self.response["intents"]['intent'], bd=2, justify="left")
        intents_intent.grid(row=3, column=1, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        h3_2 = tk.Label(self, text="Confidence:", bd=2, relief="groove", justify="center")
        h3_2.grid(row=3, column=2, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        intents_confidence = tk.Label(self, text=self.response["intents"]['confidence'], bd=2, justify="left")
        intents_confidence.grid(row=3, column=3, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        entities = tk.Label(self, text=self.response["entities"], bd=2, relief="groove", justify="left")
        entities.grid(pady=5, padx=5, columnspan=1, sticky="W" + "E")
