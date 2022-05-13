import argparse

import l15_argparse_parent_base

parser = argparse.ArgumentParser(parents=[l15_argparse_parent_base.parser],)
parser.add_argument('--local-arg', action="store_true", default=False)
print(parser.parse_args())
