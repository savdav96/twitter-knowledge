import tkinter as tk
from src.views.AppView import AppView


class AppController:

        root = tk.Tk()
        AppView(root).pack(side="top", fill="both", expand=True)
        #root.resizable(width=False, height=False)
        root.geometry("400x300")
        root.minsize(600, 300)
        root.maxsize(800, 500)
        root.deiconify()
        root.mainloop()
