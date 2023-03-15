"""Implements an Array class that supports the basic list operations."""


class Array:
    """Implements an Array class that supports the basic list operations."""

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        """Returns the item at the given index."""
        return self.data[index]

    def push(self, item):
        """Adds an item to the end of the array."""
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        """Removes the last item from the array and returns it."""
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def insert(self, index, item):
        """Inserts an item at the given index,
        shifting subsequent items right."""
        for i in range(self.length - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = item
        self.length += 1
        return self.length

    def delete(self, index):
        """Deletes the item at the given index,
        shifting subsequent items left."""
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item
