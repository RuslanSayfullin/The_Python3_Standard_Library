from queue import Queue

import threading
import time
import urllib
from urllib.parse import urlparse
import feedparser


# Установка некоторых глобальных переменных
num_fetch_threads = 2
enclosure_queue = Queue()

# В реальном приложении вы не будете задавать данные в коде...
feed_urls = [
	’http://talkpython.fm/episodes/rss ',
]

def message(s):
print(’(}: {)'.format(threading.current_thread().name, s))
