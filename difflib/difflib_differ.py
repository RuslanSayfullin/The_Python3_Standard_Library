import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(textl_lines, text2_lines)
print('\n'.join(diff))