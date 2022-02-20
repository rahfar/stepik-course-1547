from collections import deque


def main():
    max_buffer_size, n = list(map(int, input().split()))
    arrivals = []
    durations = []
    buffer = deque()

    for _ in range(n):
        _arrival, _duration = list(map(int, input().split()))
        arrivals.append(_arrival)
        durations.append(_duration)

    free_time = 0

    for i in range(len(arrivals)):
        if arrivals[i] >= free_time:
            free_time = arrivals[i] + durations[i]
            print(arrivals[i])
            buffer = deque([free_time])
        else:
            if len(buffer) < max_buffer_size:
                print(free_time)
                free_time += durations[i]
                buffer.appendleft(free_time)
            else:
                tmp = buffer.pop()
                if tmp <= arrivals[i]:
                    print(free_time)
                    free_time += durations[i]
                    buffer.appendleft(free_time)
                else:
                    buffer.append(tmp)
                    print(-1)


if __name__ == "__main__":
    main()
