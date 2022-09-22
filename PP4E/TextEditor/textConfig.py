"""
модуль с начальными настройками PyEdit (textEditor.py);
"""

#-----------------------------------------------------------------------------
# Общие настройки
# закомментируйте любые настройки в этом разделе, чтобы принять настройки по
# умолчанию библиотеки Tk или программы; шрифт/цвет можно также менять из меню
# в графическом интерфейсе, а также менять размеры окон после их открытия;
# импортируются из пути поиска модулей: могут определять отдельные настройки
# для каждого клиентского приложения, игнорируется, если находится не в пути
# поиска модулей;
#-----------------------------------------------------------------------------
# начальные настройки шрифта    # семейство, размер, стиль
font = ('courier', 9, 'normal') # например, стиль: 'bold italic'

# начальные настройки цвета     # по умолчанию = white, black
bg = 'lightcyan'                # название цвета или шестнадцатеричный код RGB
fg = 'black'                    # например, 'powder blue', '#690f96'


# начальные настройки размеров
height = 20         # умолчания Tk: 24 строки
width = 80          # умолчания Tk: 80 символов

# нечувствительность к регистру при поиске
caseinsens = True   # по умолчанию = 1/True (включена)

#-----------------------------------------------------------------------------
# 2.1: Порядок выбора кодировки для содержимого и имен файлов в операциях
# открытия и сохранения;
# опробует каждый случай из перечисленных ниже в указанном порядке, пока не
# будет обнаружен первый, дающий положительный результат; запишите во все
# переменные false/пустое значение/0, чтобы перейти к использованию умолчаний
# для вашей платформы (то есть 'utf-8' – в Windows, или 'ascii', 'latin-1'
# или другая кодировка в иных системах, таких как Unix);
# savesUseKnownEncoding: 0=Нет, 1=Да, только для операции Save, 2=Да для
# операций Save и SaveAs;
# всегда импортируются из этого файла: sys.path – если главный модуль, иначе –
# относительно пакета;
#-----------------------------------------------------------------------------

                    # 1) Сначала выполняется попытка применить известную
                    # кодировку (например, из заголовка сообщения
                    # электронной почты)
opensAskUser = True # 2) Если True, далее выполняется запрос у пользователя
                    # (предварительно заполняется значением по умолчанию)
opensEncoding = ''  # 3) Если непустое значение, далее будет выполнена попытка
                    # применить эту кодировку: 'latin-1', 'cp500'
                    # 4) Далее выполняется попытка применить
                    # sys.getdefaultencoding() - системное значение
                    # по умолчанию
                    # 5) В крайнем случае текст передается в двоичном виде и
                    # используются алгоритмы Tk

savesUseKnownEncoding = 1   # 1) Если > 0, выполняется попытка применить
                            # кодировку, известную по последней операции Open
                            # или Save
savesAskUser = True         # 2) Если True, далее выполняется запрос у
                            # пользователя (предварительно заполняется известным значением?)

savesEncoding = ''          # 3) Если непустое значение, далее будет выполнена
                            #   попытка применить эту кодировку: 'utf-8' и так далее

                            # 4) В крайнем случае выполняется попытка применить
                            # sys.getdefaultencoding()











