from re_test_patterns import test_patterns

test_patterns(
    'This is some test -- with punctuation.',
    [('[a-z]+', 'sequences of lowercase letters'),
    ('[A-Z]+', 'sequences of uppercase letters'),
    ('[a-azA-Z]+', 'sequences of lower - or uppercase  letters'),
    ('[A-Z] [a-z]+', 'one uppercase followed by lowercase')],
)