import difflib
from l63_difflib_data import *
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))
