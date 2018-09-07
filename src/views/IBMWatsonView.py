import tkinter as tk, time
from tkinter import ttk


class IMBResponseView(tk.Frame):

    def __init__(self, parent, response, data_controller, relation):
        super().__init__(parent)
        self.response = response
        self.statistics = data_controller.get_statistics()
        self.relation = relation
        self.relations = data_controller.get_relations()
        self.recognized = False
        self.known = False

        self.h6 = tk.Label(self, bd=2, relief="groove", justify="center")
        self.h6.grid(row=5, column=1, columnspan=2, pady=5, padx=5, sticky="W" + "E")
        self.known_intent_button = ttk.Checkbutton(self, text="Mark result as correctly detected (TP) or "
                                                              "correctly undetected (TN)", command=self.known_intent)
        self.known_intent_button.grid(row=4, column=1, pady=5, padx=5, columnspan=2, sticky="W" + "E")
        self.done_button = ttk.Button(self, text="Save", command=self.handle_intent)
        self.done_button.grid(row=5, column=0, pady=5, padx=5, columnspan=1, sticky="W" + "E")
        tk.Label(self, text="Input:", bd=2, justify="left") \
            .grid(row=0, column=0, pady=5, padx=5, sticky="W" + "E")
        tk.Label(self, relief="groove", text=self.response["input"]['text'], bd=2, justify="left") \
            .grid(row=0, column=1, pady=5, columnspan=2, padx=5, sticky="W" + "E")
        tk.Label(self, text="Intent:", bd=2, justify="left") \
            .grid(row=1, column=0, pady=5, padx=5, sticky="W" + "E")
        tk.Label(self, text="Confidence:", bd=2, justify="left") \
            .grid(row=2, column=0, pady=5, padx=5, sticky="W" + "E")
        print(response)

        if not (not self.response["intents"]):
            intent = self.response["intents"][0]['intent']
            confidence = self.response["intents"][0]['confidence']
            self.recognized = True
        else:
            intent = "Not found"
            confidence = "..."

        tk.Label(self, relief="groove", text=intent, bd=2, justify="left")\
            .grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="W" + "E")
        tk.Label(self, relief="groove", text=confidence, bd=2, justify="left")\
            .grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="W" + "E")

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
