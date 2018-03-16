from tkinter import *
from tkinter import messagebox
from script_tweepy import Searcher
class Application(Frame):

    def SubmitController(self):
        query=self.INPUT.get()
        print("You wrote: "+ query)
        Searcher.results(q=query)

    def QuitController(self):
        messagebox.showwarning("Attenzione", "Usa la X in alto a destra")

    def createWidget(self):
        self.QUIT = Button(text="QUIT", command=self.QuitController, fg="red")
        self.SUBMIT = Button(text="Submit", command=self.SubmitController)
        self.TEXT = Label(text="Write the search query:", font=("Helvetica",10))
        self.INPUT = Entry()
        self.visualizer()

    def visualizer(self):
        self.QUIT.pack({"side": "left"})
        self.SUBMIT.pack({"side": "right"})
        self.TEXT.pack({"side": "left"})
        self.INPUT.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()

root = Tk()
root.title("Twitter search")
root.geometry("+400+300")
root.resizable(False, False)
app = Application(master=root)
app.mainloop()
root.destroy()

