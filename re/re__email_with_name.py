import re

address = re.compile(
    '''
    
    ''')

candidates = [
    u'first.last@example.com' ,
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    u'<first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')