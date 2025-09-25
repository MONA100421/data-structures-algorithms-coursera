# python3
import sys

# ----- suffix array (prefix-doubling) -----
def sort_characters(s):
    order = [0]*len(s)
    # 假設字元為一般 ASCII，直接以 ord 當 key
    alphabet = sorted(set(s))
    char_to_id = {c:i for i,c in enumerate(alphabet)}
    cnt = [0]*len(alphabet)
    for ch in s:
        cnt[char_to_id[ch]] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        cid = char_to_id[c]
        cnt[cid] -= 1
        order[cnt[cid]] = i
    return order, char_to_id

def compute_char_classes(s, order):
    cls = [0]*len(s)
    cls[order[0]] = 0
    for i in range(1, len(s)):
        cur, prev = order[i], order[i-1]
        if s[cur] != s[prev]:
            cls[cur] = cls[prev] + 1
        else:
            cls[cur] = cls[prev]
    return cls

def sort_doubled(s, L, order, cls):
    n = len(s)
    cnt = [0]*n
    new_order = [0]*n
    for i in range(n):
        cnt[cls[i]] += 1
    for i in range(1, n):
        cnt[i] += cnt[i-1]
    for i in range(n-1, -1, -1):
        start = (order[i] - L) % n
        cl = cls[start]
        cnt[cl] -= 1
        new_order[cnt[cl]] = start
    return new_order

def update_classes(order, cls, L):
    n = len(order)
    new_cls = [0]*n
    new_cls[order[0]] = 0
    for i in range(1, n):
        cur, prev = order[i], order[i-1]
        mid, mid_prev = (cur + L) % n, (prev + L) % n
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_cls[cur] = new_cls[prev] + 1
        else:
            new_cls[cur] = new_cls[prev]
    return new_cls

def suffix_array(s: str):
    order, _ = sort_characters(s)
    cls = compute_char_classes(s, order)
    L = 1
    n = len(s)
    while L < n:
        order = sort_doubled(s, L, order, cls)
        cls = update_classes(order, cls, L)
        L <<= 1
    return order

# ----- BWT -----
def BWT(text: str) -> str:
    """
    Burrows–Wheeler transform:
    BWT[i] = text[(sa[i] - 1) mod n]
    """
    sa = suffix_array(text)
    n = len(text)
    out = []
    for p in sa:
        out.append(text[(p - 1) % n])
    return ''.join(out)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
