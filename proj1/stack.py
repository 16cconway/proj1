class Stack:
    def __init__(self):
        """
        This class is used to hold elements in a traditional stack.
        :param: self
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Determines if the stack is currently holding any items
        :return: True if the stack currently has no items
        """
        return len(self.items) == 0

    def pop(self) -> str:
        """
        Removes one item from the top of the stack and returns it.
        :return: The current item on top of the stack.
        """
        return self.items.pop()

    def push(self, insert_me) -> None:
        """
        Pushes an element onto the stack
        :param: insert_me: the element to insert.
        """
        self.items.append(insert_me)

    def peek(self) -> bool:
        """
        Checks the top item of the stack
        :return: the top item of the stack
        """
        if self.is_empty():
            raise ValueError("Stack contains no items")
        else:
            last_item = self.items[-1]
            return last_item

    def empty(self) -> None:
        """
        Empties the stack of all items
        """

        while not self.is_empty():
            self.pop()
