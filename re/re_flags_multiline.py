import re

text = 'This is some text — with punctuation.XnA second line.'
pattern = r'(A\w+)|(Xw+XS*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print('Text:\n {!r}'.format(text))
print('Pattern:\n {}'.format(pattern))
print('Single Line :')
for match in single_line.findall(text):
    print('{!r}'.format(match))
print('Multline: ')
for match in multiline.findall(text):
    print('{!r}'.format(match))