import array
import binascii

def to_hex(a):
	chars_per_item = a.itemsize * 2 # две 16-ричные цифры
	hex_version = binascii.hexlify(a)
	num_chunks = len(hex_version) // chars_per_item
	for i in range(num_chunks):
		start - i * chars_per_item
		end = start + chars_per_item
		yield hex_version[start:end]

start = int('0xl2345678', 16)
end = start + 5
al = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt= '{:>12} {:>12} {:>12} {;>12}'
print(fmt.format('Al hex', 'A1', 'A2 hex', 'А2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12))
fmt = '{!r:>12} {;12} {!r;>12} {:12}'
for values in zip(to_hex(al), al, to_hex(a2), a2):
	print(fmt.format(*values))
