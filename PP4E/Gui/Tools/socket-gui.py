# сервер GUI: читает и отображает текст, полученный
# от сценария командной строки

import sys, os
from socket import *            # включая socket.error
from tkinter import Tk
from PP4E.launchmodes import PortableLauncher
from PP4E.Gui.Tools.guiStreams import GuiOutput

myport = 50008
sockobj = socket(AF_INET, SOCK_STREAM)  # GUI - сервер, сценарий - клиент
sockobj.bind(('', myport))              # сервер настраивается перед
sockobj.listen(5)                       # запуском клиента

print('starting')
PortableLauncher('nongui', 'socket-nongui.py -gui')() # запустить сценарий
print('accepting')
conn, addr = sockobj.accept()           # ждать подключения клиента
conn.setblocking(False)                 # неблокирующий сокет (False=0)
print('accepted')


def checkdata():
    try:
        message = conn.recv(1024)
        #output.write(message + '\n')
        print(message, file=output)
    except error:
        print('no data')
    root.after(1000, checkdata)

root = Tk()
output = GuiOutput(root)        # текст из сокета отображается здесь
checkdata()
root.mainloop()

