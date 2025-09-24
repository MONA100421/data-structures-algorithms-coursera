# python3
import sys


def build_heap(data):
    swaps = []
    n = len(data)

    def sift_down(i):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right
            if smallest == i:
                break
            swaps.append((i, smallest))
            data[i], data[smallest] = data[smallest], data[i]
            i = smallest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)
    return swaps


def main():
    tokens = sys.stdin.read().split()
    if tokens and tokens[0] in ("I", "F"):
        mode = tokens[0]
        if mode == "I":
            n = int(tokens[1])
            data = list(map(int, tokens[2:2 + n]))
        else:
            fname = tokens[1]
            with open(fname, "r") as f:
                _ = f.readline()
                data = list(map(int, f.readline().split()))
            n = len(data)
    else:
        n = int(tokens[0])
        data = list(map(int, tokens[1:1 + n]))

    swaps = build_heap(data)
    out = [str(len(swaps))]
    out.extend(f"{i} {j}" for i, j in swaps)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
