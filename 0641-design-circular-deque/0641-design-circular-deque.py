class MyCircularDeque:

    def __init__(self, k: int):
        self.buffer = [0] * k
        self.capacity = k
        self.head = 0  # Points to the current front element
        self.rear = 0  # Points to the next available slot for insertLast
        self.size = 0  # Tracks current number of elements

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move head back by 1 (circular) and place the value
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.buffer[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # Place value at rear and move rear forward by 1 (circular)
        self.buffer[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Move head forward by 1 (circular)
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Move rear back by 1 (circular)
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # Rear points to the next open slot, so actual last element is at rear - 1
        return self.buffer[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()