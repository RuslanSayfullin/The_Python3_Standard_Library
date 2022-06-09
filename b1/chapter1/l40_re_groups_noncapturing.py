from l37_re_test_patterns_group import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))', 'capturing form'),
        (r'a((?:a+)|(?:b+))', 'noncapturing')],
)
