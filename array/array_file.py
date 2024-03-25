import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1: ', a)

# запись массива чисел во временный файл
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)   # нужно передать реальный файл
output.flush()

# Чтение "сырых" байтовых данных
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents: ', binascii.hexlify(raw_data))

    # Чтение данных в массив
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2: ', a2)
