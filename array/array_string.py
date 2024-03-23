import array
import binascii

S = b'This is the array'
a = array.array('b', S)

print('As byte string: ', S)
print('As array: ', a)
print('As hex: ', binascii.hexlify(a))
