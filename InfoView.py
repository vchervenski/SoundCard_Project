import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from TextFile import TextFile


class InfoView(tk.Frame):

    def start_gui(self, ok=True):
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def init_window(self):
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu, tearoff=0)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        text = Text(self, width=200, height=300)
        scroll = Scrollbar(self, command=text.yview)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack()
        text.insert(END, self.textFile.text1)
        text.configure(yscrollcommand=scroll.set, state=DISABLED)

    def client_exit(self):
        self.master.destroy()

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Information")
        self.textFile = TextFile()
        # self.grid()
        # option is needed to put the main label in the window
        self.init_window()
