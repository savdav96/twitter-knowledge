from tkinter import *
from TwitterClient import *


class View(Frame):

    def submit_controller(self):

        # Starts a Twitter stream from TwitterClient attribute

        query = self.INPUT.get()
        print("You wrote: " + query)
        self.twitter.start_stream(q=query)

    def stop_controller(self):

        # Stops the Twitter stream and quit application

        self.twitter.stop_stream()
        self.quit()

    def create_widget(self):

        # Creates widgets and packs them into the Tk() frame

        self.STOP = Button(text="STOP", command=self.stop_controller, fg="red")
        self.SUBMIT = Button(text="Submit", command=self.submit_controller)
        self.TEXT = Label(text="Write the search query:", font=("Helvetica", 10))
        self.INPUT = Entry()
        self.STOP.pack({"side": "left"})
        self.SUBMIT.pack({"side": "right"})
        self.TEXT.pack({"side": "left"})
        self.INPUT.pack({"side": "left"})

    def _callback(self):

        # Prevents from accessing X to close application

        pass

    def __init__(self):
        self.twitter = TwitterClient()
        self.root = Tk()
        Frame.__init__(self, self.root)  # Frame's constructor requires a Tk() parameter
        self.root.title("Twitter search")
        self.root.geometry("+400+300")
        self.root.protocol("WM_DELETE_WINDOW", self._callback)
        self.root.resizable(False, False)
        self.create_widget()

