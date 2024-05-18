class DynamicArray:

    # O(n) - n = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    # O(1)
    def get(self, i: int) -> int:
        return self.arr[i]
    
    # O(1)
    def insert(self, i: int, n: int) -> None:
        self.arr[i] = n

    # O(1) - Avg case / Ammortized
    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    # O(1)
    def popback(self) -> int:
        # Soft deletion
        self.size -= 1
        return self.arr[self.size]

    # O(n)
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.size

    # O(1)
    def getCapacity(self) -> int:
        return self.capacity 
    
if __name__ == "__main__":

    # Creating a DynamicArray with initial capacity of 4
    dynamic_array = DynamicArray(4)

    # Inserting elements into the array
    dynamic_array.pushback(1)
    dynamic_array.pushback(2)
    dynamic_array.pushback(3)
    dynamic_array.pushback(4)

    print(f'Array contents {[dynamic_array.get(i) for i in range(dynamic_array.getSize())]}')
    print(f'Current Size: {dynamic_array.getSize()}')
    print(f'Current capacity: {dynamic_array.getCapacity()}')

    # The array should resize here
    dynamic_array.pushback(5)
    print(f'Array contents: {[dynamic_array.get(i) for i in range(dynamic_array.getSize())]}')
    print(f'Current capacity: {dynamic_array.getCapacity()}')