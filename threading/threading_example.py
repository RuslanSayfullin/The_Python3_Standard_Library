import threading

def foo():
    print("Hello threading!")

my_thread = threading.Thread(target=foo)

my_thread.start()
