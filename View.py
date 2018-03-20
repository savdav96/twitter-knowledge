from tkinter import *

class View(Frame):

    def SubmitController(self):
        query = self.INPUT.get()
        print("You wrote: "+ query)
        TwitterClient.search(q=query)
        #TwitterClient.(self)

    def QuitController(self):
        self.quit()

    def createWidget(self):
        self.QUIT = Button(text="QUIT", command=self.QuitController, fg="red")
        self.SUBMIT = Button(text="Submit", command=self.SubmitController)
        self.TEXT = Label(text="Write the search query:", font=("Helvetica",10))
        self.INPUT = Entry()
        self.packer()

    def packer(self):
        self.QUIT.pack({"side": "left"})
        self.SUBMIT.pack({"side": "right"})
        self.TEXT.pack({"side": "left"})
        self.INPUT.pack({"side": "left"})

    def __init__(self):
        self.root = Tk()
        Frame.__init__(self, self.root)
        self.pack()
        self.root.title("Twitter search")
        self.root.geometry("+400+300")
        self.root.resizable(False, False)
        self.createWidget()
