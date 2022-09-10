# обработчики: перезагружаются перед каждым вызовом
def message1():             # изменить себя
    print('spamSpamSPAM')   # можно было бы вывести диалог...


def message2(self):     # изменить себя
    print('Ni! Ni!')    # обращение к экземпляру 'Hello'...
    self.method1()
    
    