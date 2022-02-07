def main():
    n = int(input())
    parents_list = list(map(int, input().split()))

    root = 0
    children = {i: [] for i in range(n)}
    max_height = 1
    heights = {i: 0 for i in range(n)}

    for child, parent in enumerate(parents_list):
        if parent != -1:
            children[parent].append(child)
        else:
            root = child

    queue = [root]

    while len(queue) > 0:
        node = queue.pop()
        heights[node] = (
            heights[parents_list[node]] + 1 if parents_list[node] != -1 else 1
        )
        max_height = max(max_height, heights[node])
        for child in children[node]:
            queue.insert(0, child)

    print(max_height)


if __name__ == "__main__":
    main()
