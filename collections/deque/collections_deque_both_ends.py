import collections
import threading
import time

candle = collections.deque(range(5))

def burn(directions, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(directions, next))
            time.sleep(0.1)
    print('{:>8} done'.format(directions))
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()
