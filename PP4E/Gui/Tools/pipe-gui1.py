# графический интерфейс: перенаправляет стандартный вывод порождаемой
# программы в окно GUI

from PP4E.Gui.Tools.guiStreams import redirectedGuiShellCmd     # исп-ет GuiOutput
redirectedGuiShellCmd('python -u pipe-nongui.py')               # -u: без буферизации