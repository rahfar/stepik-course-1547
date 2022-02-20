class Stack:
    def __init__(self) -> None:
        self.original_stack = []
        self.max_holding_stack = []

    def push(self, v):
        self.original_stack.append(v)

        if len(self.max_holding_stack) == 0:
            self.max_holding_stack.append(v)
        else:
            current_max = self.max_holding_stack[-1]
            if v > current_max:
                self.max_holding_stack.append(v)
            else:
                self.max_holding_stack.append(current_max)

    def pop(self):
        self.max_holding_stack.pop()
        return self.original_stack.pop()

    def max(self):
        print(self.max_holding_stack[-1])


def main():
    q = int(input())
    stack = Stack()
    for _ in range(q):
        cmd = input()
        if cmd == "max":
            stack.max()
        elif cmd == "pop":
            stack.pop()
        else:
            _, v = cmd.split()
            stack.push(int(v))


if __name__ == "__main__":
    main()
