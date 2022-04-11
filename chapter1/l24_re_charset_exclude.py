from l20_re_test_patterns import test_patterns

test_patterns(
    'This is some text — with punctuation.',
    [('[A~. ]+', 'sequences without -, ., or space')],
)
