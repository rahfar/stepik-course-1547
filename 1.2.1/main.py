def main():
    s = input()

    right_braket_pairs = {"()", "[]", "{}"}
    closing_brakets = {")", "]", "}"}
    opening_brakets = {"(", "[", "{"}
    stack = []
    i = 0
    l = len(s)

    while i < l:
        if s[i] in closing_brakets:
            ch = stack.pop()[0] if len(stack) > 0 else ""
            if ch + s[i] not in right_braket_pairs:
                print(i + 1)
                return
        elif s[i] in opening_brakets:
            stack.append((s[i], i))
        else:
            pass

        i += 1

    if len(stack) > 0:
        print(stack.pop()[1] + 1)
    else:
        print("Success")


if __name__ == "__main__":
    main()
