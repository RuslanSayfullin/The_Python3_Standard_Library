"""
##############################################################################
PyEdit 2.1: Текстовый редактор и компонент на Python/tkinter.
Использует текстовый виджет из библиотеки Tk, меню и панель инструментов
GuiMaker для реализации полнофункционального текстового редактора, который
может выполняться, как самостоятельная программа, или прикрепляться к другим
графическим интерфейсам, как компонент. Используется также в PyMailGUI
и PyView для редактирования сообщений электронной почты и примечаний к файлам
изображений. Кроме того, используется в PyMailGUI и PyDemos во всплывающем
режиме для отображения текстовых файлов и файлов с исходными текстами.

Новое в версии 2.1 (4 издание)
- работает под управлением Python 3.X (3.1)
- добавлен пункт “grep” меню и диалог: многопоточный поиск в файлах
- проверяет все окна на наличие несохраненных изменений при завершении
- поддерживает произвольные кодировки для файлов: в соответствии с настройками
в файле textConfig.py
- переработаны диалоги поиска с заменой и выбора шрифта, чтобы обеспечить
возможность одновременного вывода нескольких диалогов
- вызывает self.update() перед вставкой текста в новое окно
- различные улучшения в реализации операции Run Code, как описывается
в следующем разделе

2.1 улучшения в реализации операции Run Code:
- после команды chdir использует базовое имя запускаемого файла, а не
относительные пути
- в Windows использует инструмент запуска, поддерживающий передачу аргументов
командной строки
- операция Run Code наследует преобразование символов обратного слеша от
модуля launchmodes (необходимость в этом уже отпала)

Новое в версии 2.0 (3 издание)
- добавлен простой диалог выбора шрифта
- использует прикладной интерфейс Tk 8.4 к стеку отмен, чтобы добавить
поддержку отмены/возврата (undo/redo) операций редактирования
- запрос подтверждения при выполнении операций Quit, Open, New, Run
выполняется, только если имеются несохраненные изменения
- поиск теперь по умолчанию выполняется без учета регистра символов
- создан модуль с настройками для начальных значений
шрифта/цвета/размера/чувствительности к регистру при поиске
TBD 1 (и предложения для самостоятельной реализации):
- необходимость учета регистра символов при поиске можно было бы задавать в
графическом интерфейсе (а не только в файле с настройками)
- при поиске по файлу или в операции Grep можно было бы использовать поддержку
регулярных выражений, реализованную в модуле re (см. следующую главу)
- можно было бы попробовать реализовать подсветку синтаксиса (как в IDLE или в
других редакторах)
- можно было бы попробовать проверить завершение работы программы методом
quit() в неподконтрольных окнах
- можно было бы помещать в очередь каждый результат, найденный в диалоге Grep,
чтобы избежать задержек
- можно было бы использовать изображения на кнопках в панели инструментов (как
в примерах из главы 9)
- можно было бы просматривать строки, чтобы определить позицию вставки Tk для
оформления отступов в окне Info
- можно было бы поэкспериментировать с проблемой кодировок в диалоге “grep”
(смотрите примечания в программном коде);
##############################################################################
"""

Version = ‘2.1’
import sys, os                                  # платформа, аргументы, инструменты запуска
from tkinter import *                           # базовые виджеты, константы
from tkinter.filedialog import Open, SaveAs     # стандартные диалоги
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor
from PP4E.Gui.Tools.guimaker import *           # Frame + построители меню/панелей инструментов

# общие настройки
try:
    import textConfig               # начальный шрифт и цвета
    configs = textConfig.__dict__   # сработает, даже если модуль отсутствует в
except:                             # пути поиска или содержит ошибки
    configs = {}

helptext = """PyEdit, версия %s
апрель, 2010
(2.0: январь, 2006)
(1.0: октябрь, 2000)

Программирование на Python, 4 издание
Марк Лутц (Mark Lutz), для издательства O’Reilly Media, Inc.
Программа и встраиваемый компонент текстового редактора,
написанный на Python/tkinter. Для быстрого доступа к операциям
использует отрывные меню, панели инструментов и горячие клавиши в меню.
ополнения в версии %s:
- поддержка 3.X
- новый диалог “grep” поиска во внешних файлах
- проверка несохраненных изменений при завершении
- поддержка произвольных кодировок для файлов
- допускает одновременный вывод нескольких диалогов
поиска с заменой и выбора шрифта
- различные улучшения в операции Run Code
Дополнения в предыдущей версии:
- диалог выбора шрифта
- неограниченное количество отмен/возвратов
- quit/open/new/run предлагают сохранить, только
если есть несохраненные изменения
- поиск выполняется без учета регистра символов
- модуль с начальными настройками textConfig.py
"""

START = ‘1.0’               # индекс первого символа: строка=1,столбец=0
SEL_FIRST = SEL + ‘.first’  # отобразить тег sel в индекс
SEL_LAST = SEL + ‘.last’    # то же, что ‘sel.last’


FontScale = 0                   # использовать увеличенный шрифт в Linux
if sys.platform[:3] != ‘win’:   # и в других не-Windows системах
    FontScale = 3

##############################################################################
# Главные классы: реализуют графический интерфейс редактора, операции
# разновидности GuiMaker должны подмешиваться в более специализированные
# подклассы, а не наследоваться непосредственно, потому что этот класс
# принимает множество форм.
##############################################################################

class TextEditor:       # смешать с классом Frame, имеющим меню/панель инструментов
    startfiledir = ‘.’  # для диалогов
    editwindows = []    # для проверки при завершении
    # Настройки порядка выбора кодировки
    # импортируется в класс, чтобы обеспечить возможность переопределения в
    # подклассе

    if __name__ == ‘__main__’:
        from textConfig import ( # мой каталог в пути поиска
            opensAskUser, opensEncoding,
            savesUseKnownEncoding, savesAskUser, savesEncoding)
    else:
        from .textConfig import ( # 2.1: всегда из этого пакета
            opensAskUser, opensEncoding,
            savesUseKnownEncoding, savesAskUser, savesEncoding)

    ftypes = [(‘All files’, ‘*’),       # для диалога открытия файла
            (‘Text files’, ‘.txt’),     # настроить в подклассе или
            (‘Python files’, ‘.py’)]    # устанавливать в каждом экземпляре

    colors = [{‘fg’:’black’, ‘bg’:’white’}, # список цветов для выбора
                {‘fg’:’yellow’, ‘bg’:’black’}, # первый элемент по умолчанию
                {‘fg’:’white’, ‘bg’:’blue’}, # переделать по-своему или
                {‘fg’:’black’, ‘bg’:’beige’}, # использовать элемент выбора
                {‘fg’:’yellow’, ‘bg’:’purple’},# PickBg/Fg
                {‘fg’:’black’, ‘bg’:’brown’},
                {‘fg’:’lightgreen’, ‘bg’:’darkgreen’},
                {‘fg’:’darkblue’, ‘bg’:’orange’},
                {‘fg’:’orange’, ‘bg’:’darkblue’}]

    fonts = [(‘courier’,        9+FontScale,  ‘normal’),    # шрифты, нейтральные
                (‘courier’,     12+FontScale, ‘normal’),    # в отношении платформы
                (‘courier’,     10+FontScale, ‘bold’),      # (семейство, размер, стиль)
                (‘courier’,     10+FontScale, ‘italic’),    # или вывести в списке
                (‘times’,       10+FontScale, ‘normal’),    # увеличить в Linux
                (‘helvetica’,   10+FontScale, ‘normal’),    # использовать
                (‘ariel’,       10+FontScale, ‘normal’),    # ‘bold italic’ для 2
                (‘system’,      10+FontScale, ‘normal’),    # а также ‘underline’
                (‘courier’,     20+FontScale, ‘normal’)]


    def __init__(self, loadFirst=’’, loadEncode=’’):
        if not isinstance(self, GuiMaker):
            raise TypeError(‘TextEditor needs a GuiMaker mixin’)
        self.setFileName(None)
        self.lastfind = None
        self.openDialog = None
        self.saveDialog = None
        self.knownEncoding = None   # 2.1 кодировки: заполняется Open или Save
        self.text.focus()           # иначе придется щелкнуть лишний раз
        if loadFirst:
            self.update()                       # 2.1: иначе строка 2;
            self.onOpen(loadFirst, loadEncode)  # см. описание в книге

    def start(self):                                        # вызывается из GuiMaker.__init__
        self.menuBar = [                                    # настройка меню/панелей
                    (‘File’, 0,                             # определение дерева меню GuiMake
                         [(‘Open...’,   0, self.onOpen),    # встроен. метод для self
                         (‘Save’,       0, self.onSave),    # метка, клавиша, обработчик
                         (‘Save As...’, 5, self.onSaveAs),
                         (‘New’,        0, self.onNew),
                         ‘separator’,
                         (‘Quit...’,    0, self.onQuit)]
                     ),
                    (‘Edit’,    0,
                        [(‘Undo’,   0, self.onUndo),
                        (‘Redo’,    0,  self.onRedo),
                        ‘separator’,
                        (‘Cut’,     0, self.onCut),
                        (‘Copy’,    1, self.onCopy),
                        (‘Paste’,   0, self.onPaste),
                        ‘separator’,
                        (‘Delete’,  0, self.onDelete),
                        (‘Select All’, 0, self.onSelectAll)]
                    ),
                    (‘Search’, 0,
                        [(‘Goto...’, 0, self.onGoto),
                        (‘Find...’, 0, self.onFind),
                        (‘Refind’, 0, self.onRefind),
                        (‘Change...’, 0, self.onChange),
                        (‘Grep...’, 3, self.onGrep)]
                    ),
                    (‘Tools’, 0,
                        [(‘Pick Font...’, 6, self.onPickFont),
                            (‘Font List’, 0, self.onFontList),
                            ‘separator’,
                            (‘Pick Bg...’, 3, self.onPickBg),
                            (‘Pick Fg...’, 0, self.onPickFg),
                            (‘Color List’, 0, self.onColorList),
                            ‘separator’,
                            (‘Info...’, 0, self.onInfo),
                            (‘Clone’, 1, self.onClone),
                            (‘Run Code’, 0, self.onRunCode)]
                        )]
        self.toolBar = [
            (‘Save’, self.onSave, {‘side’: LEFT}),
            (‘Cut’, self.onCut, {‘side’: LEFT}),
            (‘Copy’, self.onCopy, {‘side’: LEFT}),
            (‘Paste’, self.onPaste, {‘side’: LEFT}),
            (‘Find’, self.onRefind, {‘side’: LEFT}),
            (‘Help’, self.help, {‘side’: RIGHT}),
            (‘Quit’, self.onQuit, {‘side’: RIGHT})]

        def makeWidgets(self):                              # вызывается из GuiMaker.__init__
            name = Label(self, bg=’black’, fg =’white’)     # ниже меню, выше панели
            name.pack(side=TOP, fill=X)                     # компоновка меню/панелей
                                                            # фрейм GuiMaker
                                                            # компонуется сам
            vbar = Scrollbar(self)
            hbar = Scrollbar(self, orient=’horizontal’)
            text = Text(self, padx=5, wrap=’none’)  # запретить перенос строк
            text.config(undo=1, autoseparators=1)  # 2.0, по умолчанию 0, 1
            vbar.pack(side=RIGHT, fill=Y)
            hbar.pack(side=BOTTOM, fill=X)
            # скомпоновать Text последним
            text.pack(side=TOP,
                      fill=BOTH, expand=YES)  # иначе обрежутся полосы
            # прокрутки
            text.config(yscrollcommand=vbar.set)  # вызывать vbar.set при
            text.config(xscrollcommand=hbar.set)  # перемещении по тексту
            vbar.config(command=text.yview)  # вызывать text.yview при прокрутке
            hbar.config(command=text.xview)  # или hbar[‘command’]=text.xview





