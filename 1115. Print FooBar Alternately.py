from typing import Callable
import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_turn = threading.Semaphore(1)
        self.bar_turn = threading.Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.foo_turn.acquire()

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.bar_turn.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.bar_turn.acquire()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.foo_turn.release()


def printFoo() -> None:
    print("foo", end="")

def printBar() -> None:
    print("bar", end="")


n = 2
obj = FooBar(n)

t1 = threading.Thread(target=obj.foo, args=(printFoo,))
t2 = threading.Thread(target=obj.bar, args=(printBar,))

t1.start()
t2.start()

t1.join()
t2.join()

print()