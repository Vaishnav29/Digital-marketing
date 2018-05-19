from tkinter import *

my_window = Tk()

lb = Listbox(my_window)

lb.insert(1, 'Fri, 13 Oct 2017')
lb.insert(2, 'Sat, 14 Oct 2017')
lb.insert(3, 'Sun, 15 Oct 2017')
lb.insert(4, 'Mon, 16 Oct 2017')
lb.insert(5, 'Tues, 17 Oct 2017')
lb.insert(6, 'Wed, 18 Oct 2017')
lb.insert(7, 'Thurs, 19 Oct 2017')
lb.insert(8, 'Latest')

lb.place(relx = 0.5, rely = 0.5, anchor="center")

my_window.mainloop()