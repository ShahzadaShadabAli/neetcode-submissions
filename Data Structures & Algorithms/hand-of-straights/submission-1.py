class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        counts = Counter(hand)
        minHeap = list(counts.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]

            if counts[start] == 0:
                heapq.heappop(minHeap)
                continue
            
            for i in range(start, start+groupSize):
                if counts[i] <= 0:
                    return False
                counts[i]-=1
        return True