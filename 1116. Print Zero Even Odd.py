from typing import Callable
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.odd_sem = threading.Semaphore(0)
        self.even_sem = threading.Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)

            if i % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()


def printNumber(x):
    print(x, end="")


n = 2
obj = ZeroEvenOdd(n)

t1 = threading.Thread(target=obj.zero, args=(printNumber,))
t2 = threading.Thread(target=obj.even, args=(printNumber,))
t3 = threading.Thread(target=obj.odd, args=(printNumber,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print()