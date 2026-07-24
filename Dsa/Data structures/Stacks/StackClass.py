class Stack:
    """
    Represents a Stack data structure following the LIFO principle.

    LIFO (Last In, First Out) means the last element added to the stack
    is the first element removed.

    This stack supports common operations:
    - push(): Add an element to the top of the stack.
    - pop(): Remove and return the top element.
    - peek(): View the top element without removing it.
    - is_empty(): Check whether the stack is empty.
    - size(): Return the number of elements in the stack.

    Attributes:
        items (list): Stores the elements of the stack.

    Example:
        stack = Stack()

        stack.push(10)
        stack.push(20)

        print(stack.peek())  # Output: 20

        stack.pop()          # Removes 20
    """

    def __init__(self):
        self.stack = []

    def __str__(self):
        return "Stack(Top-> bottom)" + str(self.stack[::-1])

    def __len__(self):
        return len(self.stack)

    def __iter__(self):
        return iter(self.stack)

    def __contains__(self, item):
        return item in self.stack

    def push(self , item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        return None
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

    def search(self , x):
        for index , value in enumerate(self.stack):
            if value == x:
                return (index , True)

        return False

    
