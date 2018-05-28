import tkinter as tk


class TweetsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        header = tk.Label(self, text="Highlight a result and press 'Ask IBMWatson' button:", bd=2, relief="groove")
        header.pack(side="top", fill="x")
        self.listbox = tk.Listbox(self, width=200, height=50)
        scrollbar = tk.Scrollbar(self)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="bottom", fill="both", expand=True)