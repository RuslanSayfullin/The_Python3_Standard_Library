import sys
import l40_sys_shelve_importer


def show_module_details(module):
    print(' message:', module.message)
    print(' __name__:', module.__name__)
    print(' __package__:', module.__package__)
    print(' __file__:', module.__file__)
    print(' __path__:', module.__path__)
    print(' __loader__ :', module.__loader__)


filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(l40_sys_shelve_importer.ShelveFinder)
sys.path.insert(0, filename)
print('Import of "package.module1":')
import package.module1

print()
print('Examine package.module1 details:')
show_module_details(package.module1)

print()
print('Import of "package.subpackage.module2":')
import package.subpackage.module2

print()
print('Examine package.subpackage.module2 details:')
show_module_details(package.subpackage.module2)
