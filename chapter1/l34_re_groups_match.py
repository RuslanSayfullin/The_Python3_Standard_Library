import re

text = 'This is some text — with punctuation.'
print(text)
print()

patterns = [
    (r'A(\w+)', 'word at start of string'),
    (r'(\w+)\S*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
    (r'(Xw+t)Xb', 'word ending with t'),
]
for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print(' ', match.groups())
    print()
