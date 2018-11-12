import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from InfoView import InfoView


class MainAppView(tk.Frame):

    def start_gui(self, ok=True):
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def init_window(self):
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu, tearoff=0)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        # create the info object)
        info = Menu(menu, tearoff=0)
        info.add_command(label="Open info", command=self.show_info)
        menu.add_cascade(label="Info", menu=info)

        # Entries and labels
        labelFreq = Label(self, text="Frequency [Hz]:")
        labelFreq.pack()

        self.freq = Entry(self)
        self.freq.pack()
        self.freq.insert(0, "1")

        labelDuration = Label(self, text="Duration [s]:")
        labelDuration.pack()

        self.duration = Entry(self)
        self.duration.pack()
        self.duration.insert(0, "5")

        labelVolume = Label(self, text="Volume [%]:")
        labelVolume.pack()

        self.volume = Entry(self)
        self.volume.pack()
        self.volume.insert(0, "100")

        # Buttons
        self.gen = tk.Button(self)
        self.gen.pack()
        self.gen["text"] = "Generate"

        self.vis = tk.Button(self)
        self.vis.pack()
        self.vis["text"] = "Visualize"

        self.variable = StringVar()
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W, textvariable=self.variable, font=('arial', 10, 'normal'))
        self.variable.set('No work being done.')
        self.label.pack(side=BOTTOM, fill=X)
        self.pack()

        WAVES = [
            ("Sine Wave", "1"),
            ("Square Wave", "2"),
            ("Sawtooth Wave", "3"),
            ("Triangle Wave", "4"),
            ("White Noise", "5")
        ]
        self.v = IntVar()
        self.v.set("1")
        for text, mode in WAVES:
            radioB = Radiobutton(self, text=text, variable=self.v, value=mode)
            radioB.pack(side='left')

    def client_exit(self):
        exit()

    def show_info(self):
        self.infoWindow = Toplevel(self.master)
        self.infoView = InfoView(self.infoWindow)

    def error_msg(self, msg):
        messagebox.showerror("Error", msg)

    def update_statusbar(self, work):
        self.variable.set(work)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        # self.grid()
        # option is needed to put the main label in the window
        self.init_window()


    


