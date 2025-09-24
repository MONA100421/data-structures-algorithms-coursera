# python3
import sys

def main():
    n = int(sys.stdin.readline())
    book = {}
    out = []
    for _ in range(n):
        parts = sys.stdin.readline().split()
        t = parts[0]
        if t == 'add':
            number = int(parts[1]); name = parts[2]
            book[number] = name
        elif t == 'del':
            number = int(parts[1])
            if number in book:
                del book[number]
        else:  # find
            number = int(parts[1])
            out.append(book.get(number, 'not found'))
    print('\n'.join(out))

if __name__ == "__main__":
    main()
