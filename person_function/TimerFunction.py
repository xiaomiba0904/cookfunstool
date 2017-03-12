#coding:utf-8
import time


class Timer:
    '''
    秒表计时器
    '''
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Already started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def test_countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    t1 = Timer()
    with t1:
        test_countdown(1000)
    print(t1.elapsed)

    with Timer() as t2:
        test_countdown(10000)
    print(t2.elapsed)