def fast_count_segments(starts, ends, points):
    events = []
    # L: segment start, R: segment end, P: query point
    # tie-breaking: L < P < R
    for s in starts:
        events.append((s, 0, None))  # L -> 0
    for e in ends:
        events.append((e, 2, None))  # R -> 2
    for idx, p in enumerate(points):
        events.append((p, 1, idx))   # P -> 1
    events.sort()

    active = 0
    ans = [0]*len(points)
    for x, typ, idx in events:
        if typ == 0:        # start
            active += 1
        elif typ == 2:      # end
            active -= 1
        else:               # point
            ans[idx] = active
    return ans

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split()))
    s, p = data[0], data[1]
    starts = data[2:2+s]
    ends = data[2+s:2+2*s]
    pts = data[2+2*s:2+2*s+p]
    print(*fast_count_segments(starts, ends, pts))
