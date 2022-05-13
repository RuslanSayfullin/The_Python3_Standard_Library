import argparse
import l20_argparse_parent_with_group

parser = argparse.ArgumentParser(parents=[l20_argparse_parent_with_group.parser],)
parser.add_argument('--local-arg', action="store_true", default=False)
print(parser.parse_args())
