import tkinter as tk


class GraphsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        header = tk.Label(self, text="Choose the kind of graph you want to print:", bd=2, relief="groove")
        header.pack(side="top", fill="x")
        self.listbox = tk.Listbox(self, width=200, height=5)
        scrollbar = tk.Scrollbar(self)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="bottom", fill="both", expand=True)