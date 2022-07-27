from tkinter import *
from gui7 import HelloPackage    # или from gui7c, где добавлен __getattr__

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
part.pack(side=RIGHT)   # НЕУДАЧА! Должно быть part.top.pack(side=RIGHT)
frm.mainloop()
