# графический интерфейс: действует так же, как pipes-gui1, но явно создает
# главное окно и запускает цикл событий
from tkinter import *
from PP4E.Gui.Tools.guiStreams import redirectedGuiShellCmd
def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()