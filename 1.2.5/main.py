import typing as t


class Stack:
    def __init__(self) -> None:
        self.original_stack: t.List[int] = []
        self.max_holding_stack: t.List[int] = []

    def push(self, v: int) -> None:
        self.original_stack.append(v)

        if len(self.max_holding_stack) == 0:
            self.max_holding_stack.append(v)
        else:
            current_max = self.max_holding_stack[-1]
            if v > current_max:
                self.max_holding_stack.append(v)
            else:
                self.max_holding_stack.append(current_max)

    def pop(self) -> int:
        self.max_holding_stack.pop()
        return self.original_stack.pop()

    def max(self) -> int:
        return self.max_holding_stack[-1]


class Queue:
    def __init__(self) -> None:
        self._left_stack = Stack()
        self._right_stack = Stack()

    def push_left(self, v: int) -> None:
        self._left_stack.push(v)

    def pop_right(self) -> int:
        if len(self._right_stack.original_stack) == 0:
            while len(self._left_stack.original_stack) > 0:
                self._right_stack.push(self._left_stack.pop())
        return self._right_stack.pop()

    def max(self) -> int:
        if len(self._right_stack.original_stack) == 0:
            return self._left_stack.max()
        elif len(self._left_stack.original_stack) == 0:
            return self._right_stack.max()
        else:
            return max(
                self._left_stack.max(),
                self._right_stack.max(),
            )


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = Queue()
    result = []

    for k in range(0, m):
        q.push_left(a[k])
    result.append(q.max())

    for i in range(1, n - m + 1):
        q.push_left(a[i + m - 1])
        q.pop_right()
        result.append(q.max())

    print(*result)


if __name__ == "__main__":
    main()
