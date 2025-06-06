from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a*)(b*))',
    'а followed by 0-n а and 0-n b')],
)