import traceback
import sys

from l47_traceback_example import produce_exception

print('with no exception:')
exc_type, exc_value, exc_tb = sys.exc_info()
tbe = traceback.TracebackException(exc_type, exc_value, exc_tb)
print(''.join(tbe.format()))

print('\nwith exception:')
try:
    produce_exception()
except Exception as err:
    exc_type, exc_value, exc_tb = sys.exc_info()
    tbe = traceback.TracebackException(exc_type, exc_value, exc_tb, )
    print(''.join(tbe.format()))

    print('\nexception only:')
    print(''.join(tbe.format_exception_only()))
    