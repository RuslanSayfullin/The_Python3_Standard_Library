import demopkg1
print('demopkg1:', demopkg1.__file__)

try:
    import demopkg1.shared
except Exception as err:
    print('demopkg1.shared : Not found ({})'.format(err))
else:
    print('demopkg1.shared :', demopkg1.shared.__file__)
try:
    import demopkg1.not_shared
except Exception as err:
    print('demopkg1.not_shared: Not found ({})'.format(err))
else:
    print('demopkg1.not_shared:', demopkg1.not_shared.__file__)
    