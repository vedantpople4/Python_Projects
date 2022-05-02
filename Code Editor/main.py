from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TEXT EDITOR")
        self.root.geometry("1200X700 + 200+150")
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()

        self.titlebar = Label(self.root, textvariable=self.title, font=("Times new roman", 15,"bold"),bd=2, relief=GROOVE)
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.status.set("Welcome to Text Editor")

        self.menubar = Menu(self.root, font=("times new roman",15,"bold"))