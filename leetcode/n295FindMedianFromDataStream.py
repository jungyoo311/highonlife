import heapq
class MedianFinder:

    def __init__(self):
        '''
        Two heap approach
        ->even
        [1,2,3,4] : median = (2+3)/2 = 2.5
        first-half: [1,2], second-half: [3,4]
        SOL: (maxHeap.pop() + minHeap.pop()) / 2 = (2+3)/2 = 2.5
        ->odd
        [1,2,3,4,5] : median = 3
        first-half: [1,2,3], second-half: [4,5]
        SOL: maxHeap.pop() = 3

        -> key takeaway: always keep: len(maxHeap) - len(minHeap) <= 1
        '''
        self.maxHeap = [] # first half
        self.minHeap = [] # second half
        
    def addNum(self, num: int) -> None:
        # Step 1 : add the elem in the maxHeap for default.
        heapq.heappush(self.maxHeap, -num)
        # Step 2 : If the top maxHeap > top minHeap, rebalance
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        # Step 3: size rebalance
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        # Step 4: 
        # [-1]
        # [2,3]
        # in this case, 2 has to be moved to maxHeap from minHeap
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return float(-self.maxHeap[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()