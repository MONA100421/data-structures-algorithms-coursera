# python3
from collections import namedtuple, deque

Request  = namedtuple("Request",  ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()  # queue of finish times (increasing)

    def process(self, request):
        t, p = request.arrived_at, request.time_to_process

        while self.finish_time and self.finish_time[0] <= t:
            self.finish_time.popleft()

        if len(self.finish_time) >= self.size:
            return Response(True, -1)

        start_time = t if not self.finish_time else max(t, self.finish_time[-1])
        self.finish_time.append(start_time + p)
        return Response(False, start_time)


def process_requests(requests, buffer):
    return [buffer.process(req) for req in requests]


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for r in responses:
        print(r.started_at if not r.was_dropped else -1)


if __name__ == "__main__":
    main()
