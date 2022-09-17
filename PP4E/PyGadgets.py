"""
##############################################################################
Запускает различные примеры; запускайте сценарий при загрузке системы, чтобы
сделать их постоянно доступными.
Этот файл предназначен для запуска программ, действительно необходимых в работе;
для запуска демонстрационных программ Python/Tk и получения дополнительных
сведений о параметрах запуска программ обращайтесь к сценарию PyDemos. Замечание
о работе в Windows: это файл с расширением '.py', поэтому при его запуске щелчком
мыши выводится окно консоли, которое используется для вывода начального сообщения
(включая 10-секундную паузу, чтобы обеспечить его видимость, пока запускаются
приложения). Чтобы избежать вывода окна консоли, запускайте сценарий с помощью
программы 'pythonw' (а не 'python'), используйте расширение '.pyw', в свойствах
ярлыка в Windows выберите значение 'Свернутое в значок' ('run minimized') в поле
'Окно' ('Window') или запускайте файл из другой программы (см. PyDemos).
##############################################################################
"""

import sys, time, os, time
from tkinter import *
from launchmodes import PortableLauncher    # повторное использ. класса запуска
from Gui.Tools.windows import MainWindow    # повторное использ. оконных
                                            # инструментов: ярлык, обработчик
                                            # закрытия окна

def runImmediate(mytools):
    """
    немедленный запуск программ
    """
    print('Starting Python/Tk gadgets...')      # вывод в stdout (временный)
    for (name, commandLine) in mytools:
        PortableLauncher(name, commandLine)()   # сразу вызвать для запуска
    print('One moment please...')
    if sys.platform[:3] == 'win':               # windows: закрыть консоль через
        for i in range(10):                     # 10 секунд
            time.sleep(1); print('.' * 5 * (i+1))

def runLauncher(mytools):
    """
    создать простую панель запуска для использования в дальнейшем
    """
    root = MainWindow('PyGadgets PP4E') # или root = Tk()
    for (name, commandLine) in mytools:
        b = Button(root, text=name, fg='black', bg='beige', border=2,
                    command=PortableLauncher(name, commandLine))
        b.pack(side=LEFT, expand=YES, fill=BOTH)
    root.mainloop()


mytools = [
    ('PyEdit', 'Gui/TextEditor/textEditor.py'),
    ('PyCalc', 'Lang/Calculator/calculator.py'),
    ('PyPhoto', 'Gui/PIL/pyphoto1.py Gui/PIL/images'),
    ('PyMail', 'Internet/Email/PyMailGui/PyMailGui.py'),
    ('PyClock', 'Gui/Clock/clock.py -size 175 -bg white'
                ' -picture Gui/gifs/pythonPowered.gif'),
    ('PyToe', 'Ai/TicTacToe/tictactoe.py'
                ' -mode Minimax -fg white -bg navy'),
    ('PyWeb', 'LaunchBrowser.pyw'
                ' -live index.html learning-python.com')]
                #' -live PyInternetDemos.html localhost:80')]
                #' -file')] # PyInternetDemos предполагает, что
                # локальный веб-сервер уже запущен


if __name__ == '__main__':
    prestart, toolbar = True, False
    if prestart:
        runImmediate(mytools)
    if toolbar:
        runLauncher(mytools)
