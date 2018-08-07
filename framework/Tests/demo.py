'''
Getting return value from Thread
'''



import threading
import queue

def asd(foo):
    print(foo)
    data = {
    "country abbreviation": "US",
    "places": [
        {
            "place name": "Belmont",
            "longitude": "-71.4594",
            "post code": "02178",
            "latitude": "42.4464"
        },
        {
            "place name": "Belmont",
            "longitude": "-71.2044",
            "post code": "02478",
            "latitude": "42.4128"
        }
    ],
    "country": "United States",
    "place name": "Belmont",
    "state": "Massachusetts",
    "state abbreviation": "MA"
    }

    return (data["places"][0]["place name"])
#-----------------------------------------------------------------------------------

que = queue.Queue()

t = threading.Thread(target=lambda q, arg1 : q.put(asd("foo")),args=(que,"World"))
t.start()
t.join()
result = que.get()
print(result)


'''
import Queue
from threading import Thread

def foo(bar):
    print 'hello {0}'.format(bar)
    return 'foo'

que = Queue.Queue()

t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'world!'))
t.start()
t.join()
result = que.get()
print result
It can be also easily adjusted to a multi-threaded environment:

import Queue
from threading import Thread

def foo(bar):
    print 'hello {0}'.format(bar)
    return 'foo'

que = Queue.Queue()
threads_list = list()

t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'world!'))
t.start()
threads_list.append(t)

# Add more threads here
...
threads_list.append(t2)
...
threads_list.append(t3)
...

# Join all the threads
for t in threads_list:
    t.join()

# Check thread's return value
while not que.empty():
    result = que.get()
    print result
'''