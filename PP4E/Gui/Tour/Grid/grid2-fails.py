"""
ОШИБКА -- методы pack и grid не могут одновременно использоваться в одном и том
же родительском контейнере (здесь, корневое окно)
"""

from tkinter import *
from grid2 import gridbox, packbox
root = Tk()
frm = Frame(root)
frm.pack()      # это работает
gridbox(frm)    # у gridbox должен быть собственный родитель
packbox(root)
Button(root, text='Quit', command=root.quit).pack()
mainloop()
