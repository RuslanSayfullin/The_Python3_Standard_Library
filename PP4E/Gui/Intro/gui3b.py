import sys
from tkinter import *   # lambda-выражение генерирует функцию

widget = Button(None,   # но содержит всего лишь выражение
    text='Hello event world',
    command=(lambda: print('Hello lambda world') or sys.exit()) )
widget.pack()
widget.mainloop()