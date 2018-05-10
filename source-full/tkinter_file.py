from tkinter import *
import File
window = Tk()
def input():
    s = entry1.get()
    return s

entry1 = Entry(window)
button1 = Button(window, text='GO', command=lambda: File.function(entry1.get()))

window.mainloop()