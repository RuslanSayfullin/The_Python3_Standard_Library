from l20_re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('а.', 'a followed by any one character'),
    ('b.', 'b followed by any one character'),
    ('a.*b', 'a followed by anything, ending in b'),
    ('a.*7b', 'a followed by anything, ending in b')],
)