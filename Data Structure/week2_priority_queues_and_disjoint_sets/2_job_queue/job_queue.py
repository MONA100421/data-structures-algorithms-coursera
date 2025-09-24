# python3
import sys
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # (next_free_time, worker_id)
    pq = [(0, w) for w in range(n_workers)]
    heapq.heapify(pq)

    result = []
    for duration in jobs:
        free_time, wid = heapq.heappop(pq)
        result.append(AssignedJob(wid, free_time))
        heapq.heappush(pq, (free_time + duration, wid))
    return result


def main():
    data = list(map(int, sys.stdin.read().split()))
    n_workers, n_jobs = data[0], data[1]
    jobs = data[2:]
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)
    out_lines = []
    for job in assigned_jobs:
        out_lines.append(f"{job.worker} {job.started_at}")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
