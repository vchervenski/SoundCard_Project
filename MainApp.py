import tkinter as tk
from MainAppController import MainAppController


def main():
    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')
    root.geometry("500x300")
    controller = MainAppController(root)


if __name__ == "__main__":
    main()
