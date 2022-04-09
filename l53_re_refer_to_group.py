import re
address = re.compile(
    r'''
    # The regular name
    (\w+)
    \s+
    (([\w.]+)\s+)?
    (\w+)
    # First name
    # Optional middle name or initial
    # Last name
    \s+
    <
    # The address: first_name.last_name@domain.tld
    (?P<email>
    \1
    # First name
    \.
    \4
    # Last name
    @
    [\w\d.]+\.)+
    (com|org|edu)
    49
    # Domain name prefix
    # Limit the allowed top-level domains.
    )
    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.group(1), match.group(4))
        print(' Match email:', match.group(5))
    else:
        print(' No match')