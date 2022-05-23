import importlib
import sys
import l40_sys_shelve_importer

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(l40_sys_shelve_importer.ShelveFinder)
sys.path.insert(0, filename)
print('First import of "package":')
import package
print()
print('Reloading "package":')
importlib.reload(package)
