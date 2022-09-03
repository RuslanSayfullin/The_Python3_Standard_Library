#!/usr/local/bin/python
"""
##############################################################################
реализует два набора инструментов, специфичных для типов
##############################################################################
"""

from shellgui import *              # интерфейсы, специфичные для типов
from packdlg import runPackDialog   # диалоги для ввода данных
from unpkdlg import runUnpackDialog # оба используют классы приложений


class TextPak1(ListMenuGui):
    def __init__(self):
        self.myMenu = [('Pack ', runPackDialog),        # простые функции
                        ('Unpack', runUnpackDialog),    # длина меток одинаковая
                        ('Mtool ', self.notdone)]       # метод из GuiMixin
        ListMenuGui.__init__(self)

    def forToolBar(self, label):
        return label in {'Pack ', 'Unpack'}      # синтаксис множеств в 3.x


class TextPak2(DictMenuGui):
    def __init__(self):
        self.myMenu = {'Pack ': runPackDialog,      # или использовать input...
                        'Unpack': runUnpackDialog,  # вместо диалогов ввода
                        'Mtool ': self.notdone}
        DictMenuGui.__init__(self)

if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1 and argv[1] == 'list':
        print('list test')
        TextPak1().mainloop()
    else:
        print('dict test')
        TextPak2().mainloop()