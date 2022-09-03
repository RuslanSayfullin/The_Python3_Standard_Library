#!/usr/local/bin/python
"""
##############################################################################
инструмент запуска; использует шаблоны GuiMaker, стандартный диалог завершения
GuiMixin; это просто биб­лиотека классов: чтобы вывести графический интерфейс,
запустите сценарий mytools;
##############################################################################
"""

from tkinter import *                           # импортировать виджеты
from PP4E.Gui.Tools.guimixin import GuiMixin    # импортировать quit, а не done
from PP4E.Gui.Tools.guimaker import *           # конструктор меню/панели инструментов
                                                

class ShellGui(GuiMixin, GuiMakerWindowMenu):   # фрейм + конструктор +
    def start(self):                            # подмешиваемые методы
        self.setMenuBar()                       # для компонентов использовать
        self.setToolBar()                       # GuiMaker
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")
    
    def handleList(self, event):                # двойной щелчок на списке           
        label = self.listbox.get(ACTIVE)        # получить выбранный текст
        self.runCommand(label)                  # и выполнить операцию
    
    def makeWidgets(self):                      # добавить список в середину
        sbar = Scrollbar(self)                  # связать sbar со списком
        list = Listbox(self, bg='white')        # или использ. Tour.ScrolledList
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)            # первым добавлен = посл. обрезан
        list.pack(side=LEFT, expand=YES, fill=BOTH)     # список обрез-ся первым
        for (label, action) in self.fetchCommands():    # добавляется в список,
            list.insert(END, label)                     # в меню и на панель инстр.
        list.bind('<Double-1>', self.handleList)        # установить обработчик
        self.listbox = list
    
    def forToolBar(self, label):    # поместить на панель инстр.?
        return True                 # по умолчанию = все
    
    
    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))
        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
            ('File', 0, [('Quit', -1, self.quit)]), # имя раскрывающегося меню
            ('Tools', 0, toolEntries)               # список элементов меню
        ]                                           # метка,клавиша,обработчик
    for (label, action) in self.fetchCommands():
        toolEntries.append((label, -1, action))     # добавить приложения в меню

##############################################################################
# делегирование операций шаблонным подклассам с разным способом хранения
# перечня утилит, которые в свою очередь делегируют операции
# подклассам, реализующим запуск утилит
##############################################################################


class ListMenuGui(ShellGui):
    def fetchCommands(self):    # myMenu устанавливается в подклассе
        return self.myMenu      # список кортежей (метка, обработчик)
    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd: action()


class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()
    def runCommand(self, cmd):
        self.myMenu[cmd]()
