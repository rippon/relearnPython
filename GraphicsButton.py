from tkinter import *
import tkinter.messagebox as messageBox
from tkinter import ttk

class GraphicsButton(Button):
    def __init__(self, frame, window, **kw):
        super().__init__(frame, **kw)
        self.window = window
        print("hallo from GraphicsButton class; window = " + window)





