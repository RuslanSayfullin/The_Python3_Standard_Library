from itertools import compress

alphabet = ["A", "B", "C", "D", "E", "F", "G"]
mask = [1, 0, 1, 0, 0, 1, 0]

result = compress(alphabet, mask)

print(list(result))
