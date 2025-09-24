# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []  # keep Bracket(char, position) ; position is 1-based
    for pos, ch in enumerate(text, 1):
        if ch in "([{":
            stack.append(Bracket(ch, pos))
        elif ch in ")]}":
            if not stack:
                return pos
            top = stack.pop()
            if not are_matching(top.char, ch):
                return pos

    if stack:
        return stack[0].position

    return "Success"


def main():
    text = input().rstrip()
    print(find_mismatch(text))


if __name__ == "__main__":
    main()
