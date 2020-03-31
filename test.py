from tkinter import *
from tkinter.ttk import *

root = Tk()

treeview = Treeview(root, columns=['c1', 'c2'])
treeview.pack()


for c in ['c1', 'c2']:
    treeview.heading(c, text=c, command=lambda:print(c))


root.mainloop()
