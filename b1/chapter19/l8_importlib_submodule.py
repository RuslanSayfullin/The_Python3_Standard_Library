import importlib

pkg_loader = importlib.find_loader('example')
pkg = pkg_loader.load_module()
loader = importlib.find_loader('submodule', pkg.__path__)
print('Loader:', loader)
m = loader.load_module()
print('Module:', m)
