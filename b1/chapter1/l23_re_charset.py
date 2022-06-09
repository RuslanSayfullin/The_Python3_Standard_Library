from l20_re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('[ab]', 'either а or b'),
     ('a[ab]+', 'a followed by 1 or more а or b'),
     ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)
