from threading import Lock


class Foo:

    # assumes three threads already exist to each handle one of the
    # three methods below
    # so now all we need to do to preserve ordering is to use locks
    def __init__(self):
        self.lock1 = Lock()

    def first(self, printFirst: 'Callable[[], None]') -> None:

        self.lock1.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock1.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lock1.release()
