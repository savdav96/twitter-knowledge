import tkinter as tk
from src.views.AppView import AppView


class AppController:

        root = tk.Tk()
        AppView(root).pack(side="top", fill="both", expand=True)
        root.resizable(width=False, height=False)
        root.deiconify()
        root.mainloop()
