import tkinter as tk
from tkinter import ttk


class IMBResponseView(tk.Frame):

    def __init__(self, parent, response, statistics, relation, relations):
        super().__init__(parent)
        self.response = response
        self.statistics = statistics
        self.relation = relation
        self.relations = relations
        self.recognized = False
        self.known = False
        self.known_intent_button = None
        self.done_button = None
        self.h6 = None

        h1 = tk.Label(self, text=" Here is shown the IBM Watson Response in terms of confidency:", bd=2, relief="groove", justify="center")
        h1.grid(row=0, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        h2 = tk.Label(self, text="Input:", bd=2, relief="groove", justify="center")
        h2.grid(row=1, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        input_query = tk.Label(self, text=self.response["input"]['text'], bd=2, justify="left")
        input_query.grid(row=2, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        h3 = tk.Label(self, text="Intent:", bd=2, relief="groove", justify="center")
        h3.grid(row=3, column=0, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        print(response)
        if not (not self.response["intents"]):
            intents_intent = tk.Label(self, text=self.response["intents"][0]['intent'], bd=2, justify="left")
            intents_confidence = tk.Label(self, text=self.response["intents"][0]['confidence'], bd=2, justify="left")
            self.recognized = True
        else:
            intents_intent = tk.Label(self, text="Not found", bd=2, justify="left")
            intents_confidence = tk.Label(self, text="...", bd=2, justify="left")

        intents_intent.grid(row=3, column=1, pady=5, padx=5, columnspan=1, sticky="W" + "E")
        intents_confidence.grid(row=3, column=3, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        h3_2 = tk.Label(self, text="Confidence:", bd=2, relief="groove", justify="center")
        h3_2.grid(row=3, column=2, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        entities = tk.Label(self, text=self.response["entities"], bd=2, relief="groove", justify="left")
        entities.grid(pady=5, padx=5, columnspan=1, sticky="W" + "E")

        h5 = tk.Label(self, text="Correctly recognized intent?", bd=2, relief="groove", justify="center")
        h5.grid(row=4, column=0, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        self.h6 = tk.Label(self, text="Precision = "+ str(self.statistics.get_precision()) + "\tRecall = " + str(self.statistics.get_recall()), bd=2, relief="groove", justify="center")
        self.h6.grid(row=6, column=3, pady=5, padx=5, columnspan=4, sticky="W" + "E")

        self.known_intent_button = ttk.Button(self, text="Yes", command=self.known_intent)
        self.known_intent_button.grid(row=4, column=3, pady=5, padx=5, columnspan=1, sticky="W" + "E")

        self.done_button = ttk.Button(self, text="Done", command=self.handle_intent)
        self.done_button.grid(row=6, column=1, pady=5, padx=5, columnspan=1, sticky="W" + "E")

    def known_intent(self):
        self.known = True
        self.known_intent_button.configure(state="disabled")

    def handle_intent(self):
        if self.recognized & self.known:
            self.statistics.TP += 1
            self.relation['Test result'] = "TP"
        if self.recognized & (not self.known):
            self.statistics.FP += 1
            self.relation['Test result'] = "FP"
        if (not self.recognized) & self.known:
            self.statistics.FN += 1
            self.relation['Test result'] = "FN"
        if (not self.recognized) & (not self.known):
            self.statistics.TN += 1
            self.relation['Test result'] = "TN"
        self.done_button.configure(state="disabled")
        self.relations.append(self.relation)
        self.h6.configure(text="Precision = " + str(self.statistics.get_precision()) + "\tRecall = " + str(self.statistics.get_recall()))
