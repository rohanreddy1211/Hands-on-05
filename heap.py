from typing import TypeVar, List, Optional

T = TypeVar('T')

class Heap:
    def __init__(self, arr: List[T], min_heap: bool = True) -> None:
        """
        Initializes the heap with the given array.

        :param arr: The initial array to build the heap from.
        :param min_heap: If True, build a min heap; if False, build a max heap.
        """
        self.heap: List[T] = arr
        self.is_min_heap = min_heap
        self.build_heap()

    def insert(self, value: T) -> None:
        """Inserts a new element into the heap."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i: int) -> None:
        """Maintains the heap property by bubbling up the element at index i."""
        parent = (i - 1) >> 1
        while i > 0 and self._compare(self.heap[i], self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) >> 1

    def _compare(self, child: T, parent: T) -> bool:
        """Compares two elements based on the heap type (min or max)."""
        return child < parent if self.is_min_heap else child > parent

    def heapify(self, n: int, i: int) -> None:
        """Ensures the heap property for the subtree rooted at index i."""
        largest_or_smallest = i
        left = (i << 1) + 1
        right = (i << 1) + 2

        if left < n and self._compare(self.heap[left], self.heap[largest_or_smallest]):
            largest_or_smallest = left
        if right < n and self._compare(self.heap[right], self.heap[largest_or_smallest]):
            largest_or_smallest = right
        
        if largest_or_smallest != i:
            self.heap[i], self.heap[largest_or_smallest] = self.heap[largest_or_smallest], self.heap[i]
            self.heapify(n, largest_or_smallest)

    def build_heap(self) -> None:
        """Builds the heap from the initial array."""
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def get_root(self) -> Optional[T]:
        """Returns the root element of the heap."""
        return self.heap[0] if self.heap else None

    def extract(self) -> Optional[T]:
        """Removes and returns the root element of the heap."""
        if not self.heap:
            return None
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(len(self.heap), 0)
        return root_value

    def size(self) -> int:
        """Returns the number of elements in the heap."""
        return len(self.heap)

if __name__ == '__main__':
    # Example usage
    arr = [50, 20, 30, 10, 15, 5, 25]
    min_heap = Heap(arr, min_heap=True)
    print(f'Min Heap: {min_heap.heap}')

    max_heap = Heap(arr, min_heap=False)
    print(f'Max Heap: {max_heap.heap}')

    min_heap.insert(2)
    print("Min Heap after inserting 2:", min_heap.heap)

    root = min_heap.get_root()
    print(f'Min Heap root element: {root}')

    popped_value = min_heap.extract()
    print(f'Min Heap after popping root ({popped_value}): {min_heap.heap}')
