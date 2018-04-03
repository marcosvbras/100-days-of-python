# coding=utf-8

"""Day 012 - Get in line with Deque.

    Deques are Double-ended Queues. They are Thread-safe and implement the most of methods of lists.
"""

from collections import deque

def run():
    # The argument 'maxlen' is optional
    dq = deque(range(10), maxlen=10)
    print(dq)
    # >>> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

    # Moving the last 3 elements to the beginning of the queue
    dq.rotate(3)
    print(dq)
    # >>> deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

    # Moving the first 3 elements to the end of the queue
    dq.rotate(-5)
    print(dq)
    # >>> deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1], maxlen=10)

    # Removing the last element of a full queue and added a new one on the left
    dq.appendleft(-1)
    print(dq)
    # >>> deque([-1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

    # This will add three new element to the end. The queue is full, so the
    # first three elements will be removed.
    dq.extend([11, 12, 13])
    print(dq)
    # >>> deque([4, 5, 6, 7, 8, 9, 0, 11, 12, 13], maxlen=10)

    # Adding elements on the left
    dq.extendleft([100, 200, 300])
    print(dq)
    # >>> deque([300, 200, 100, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

    # Removing the last element
    dq.pop()
    print(dq)
    # >>> deque([300, 200, 100, 4, 5, 6, 7, 8, 9], maxlen=10)

    # Removing the first element of the queue
    dq.popleft()
    print(dq)
    # >>> deque([200, 100, 4, 5, 6, 7, 8, 9], maxlen=10)

    # Adding a new element at the of the queue
    dq.append(1000)
    print(dq)
    # >>> deque([200, 100, 4, 5, 6, 7, 8, 9, 1000], maxlen=10)

if __name__ == '__main__':
    run()
