from l37_re_test_patterns_group import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a*)(b*))', 'а followed by 0-n а and 0-n b')],
)
