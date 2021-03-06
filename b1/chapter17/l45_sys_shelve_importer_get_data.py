import sys
import l40_sys_shelve_importer
import os
import pkgutil


filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(l40_sys_shelve_importer.ShelveFinder)
sys.path.insert(0, filename)
import package
readme_path = os.path.join(package.__path__[0], 'README')
readme = pkgutil.get_data('package', 'README')
# Equivalent to:
# readme = package.__loader__.get_data(readme_path)
print(readme.decode('utf-8'))
foo_path = os.path.join(package.__path__[0], 'foo')
try:

    foo = pkgutil.get_data('package', 'foo')
    # Equivalent to:
    # foo = package.__loader__.get_data(foo_path)
except IOError as err:
    print('ERROR: Could not load "foo"', err)
else:
    print(foo)
    