from tkinter import Tk, Text,Button, mainloop
from os import system
from sys import argv

def log(entry):
    root.destroy()
    system(f'cmdlog {argv[1]} "{entry}"')
    return

def main():
    global root
    root = Tk()
    root.geometry("700x300")
    root.eval('tk::PlaceWindow . center')
    root.title(f"Log Entry: "+argv[1])
    root.config(bg='#22272E')
    inputtxt = Text(
        root,
        height=11,
        width = 70,
        bg = "#2D333B",
        fg = "#ADBAC7"
    )
    button = Button(
        root,
        height = 2,
        width = 20,
        text="Enter",
        bg = "#347D39",
        activebackground = "#207030",
        fg = "#EDF5FF",
        activeforeground = "#EDF5FF",
        font = ("Helvetica", 8, "bold"),
        highlightcolor = "#3B7F3D",
        relief = "flat",
        command = lambda:log(inputtxt.get("1.0", "end-1c"))
    )
    inputtxt.pack(expand=True)
    button.pack(expand=True)
    mainloop()
    return

if __name__ == '__main__':
    main()
