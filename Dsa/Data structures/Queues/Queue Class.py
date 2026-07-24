class MyQueue:
    """
    Represents a Queue data structure following the FIFO principle.

    FIFO (First In, First Out) means the first element added to the queue
    is the first element removed.

    This queue supports common operations:
    - enqueue(): Add an element to the rear of the queue.
    - dequeue(): Remove and return the front element.
    - peek(): Return the front element without removing it.
    - rear(): Return the rear element without removing it.
    - is_empty(): Check whether the queue contains any elements.
    - clear(): Remove all elements from the queue.

    It also supports Python special methods:
    - len(queue): Return the number of elements.
    - print(queue): Return a readable string representation.
    - for item in queue: Iterate over the queue from front to rear.
    - item in queue: Check whether an element exists in the queue.

    Time Complexity:
    - Enqueue: O(1)
    - Dequeue: O(1) when implemented with collections.deque
               O(n) when implemented with a Python list using pop(0)
    - Peek: O(1)
    - Rear: O(1)
    - is_empty: O(1)
    - len: O(1)
    """

    def __init__(self):
        self.que = []

    def __str__(self):
        return str(self.que)

    def __contains__(self, item):
        for i in self.que:
            if i == item:
                return True
        return False

    def __iter__(self):
        return iter(self.que)

    def __len__(self):
        return len(self.que)

    def enqueue(self , x):
        self.que.insert(-1,x)

    def dequeue(self):
        if not self.is_empty():
            self.que.pop()
        return None

    def peek(self):
        if self.is_empty():
            return None
        return self.que[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.que[-1]

    def is_empty(self):
        return not self.que

    def clear(self):
        self.que = []

    def search(self , x):
        for index , value in enumerate(self.que):
            if value == x:
                return (index , True)

        return False