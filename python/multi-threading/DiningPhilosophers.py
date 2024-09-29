import threading
from typing import Callable

# https://leetcode.com/problems/the-dining-philosophers/


class DiningPhilosophers:
    def __init__(self):
        # the 1 passed in represents number of threads allowed to access the shared resource at a time
        self.left_fork = threading.Semaphore(1)
        self.right_fork = threading.Semaphore(1)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:
        # if philosopher + 1 and philosopher - 1 arent eating, then lock this thread and pick up left and right forks and eat then put back left and right forks
        with self.left_fork:
            pickLeftFork()
            with self.right_fork:
                pickRightFork()
                eat()
                putRightFork()
            putLeftFork()
