import tkinter as tk
from MainAppController import MainAppController


def main():
    controller = MainAppController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')
    root.geometry("500x300")
    controller.init_view(root)


if __name__ == "__main__":
    main()
