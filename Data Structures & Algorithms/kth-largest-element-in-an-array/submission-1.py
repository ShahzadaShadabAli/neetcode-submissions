import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Negate values to convert min-heap behavior to max-heap
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        
        # Pop the largest k - 1 elements
        for _ in range(k - 1):
            heapq.heappop(max_heap)
            
        # Root now holds the k-th largest element (negate back)
        return -max_heap[0]