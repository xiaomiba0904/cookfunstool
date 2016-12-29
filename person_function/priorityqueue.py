import heapq
import threading

class PriorityQueue:
    '''线程安全的优先级队列'''
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self,item,priority):
        with self._cv:
            heapq.heappush(self._queue, (item, self._count, -priority))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
        return heapq.heappop(self._queue)[0]