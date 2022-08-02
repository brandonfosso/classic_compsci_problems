"""
Classic Computer Science Problems in Python
Chapter 1: Small Problems
Section 5: The Towers of Hanoi
"""
from typing import Generic, List, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(
    begin: Stack[int],
    end: Stack[int],
    temp: Stack[int],
    n: int,
) -> None:
    if n == 1:
        print("move disc")
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)

    print(tower_a)
    print(tower_b)
    print(tower_c)

    hanoi(tower_a, tower_c, tower_b, num_discs)

    print(tower_a)
    print(tower_b)
    print(tower_c)
