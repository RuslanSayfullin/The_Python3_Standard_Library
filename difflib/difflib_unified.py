import difflib
from difflib_data import *

diff = difflib.unified_diff(
    textl_lines,
    text2_lines,
    lineterm='',
)
print('\n'.join(list(diff)))