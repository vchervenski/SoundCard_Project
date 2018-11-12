from MainAppView import MainAppView
from Visualize import Visualise
from Generate import Generate


class MainAppController(object):

    def visual(self):
        if self.check is None:
            self.mainView.error_msg("No graph found!")
        else:
            self.mainView.update_statusbar("Visualizing graph...")
            start = Visualise()
            start.start_visualizing(self.check)

    def generate(self):
        freq = self.mainView.freq.get()
        duration = self.mainView.duration.get()
        volume = self.mainView.volume.get()

        if freq == "0" or duration == "0" or volume == "0":
            self.mainView.error_msg("Enter a non zero value!")
        else:
            start = Generate(int(duration), int(freq), int(volume))
            self.check = start.start_gen(self.choose_wave())
            self.mainView.update_statusbar("File generated!")

    def choose_wave(self):
        return self.mainView.v.get()

    def init_view(self, root):
        self.check = None
        self.mainView = MainAppView(master=root)

        self.mainView.gen["command"] = self.generate
        self.mainView.vis["command"] = self.visual

        # Start the gui
        self.mainView.start_gui()

