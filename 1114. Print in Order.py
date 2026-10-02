from threading import Event

class Foo:
    def __init__(self):
        self.fristDone =  Event()
        self.SecondDone =  Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.fristDone.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.fristDone.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.SecondDone.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.SecondDone.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

