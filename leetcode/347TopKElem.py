class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        sort them in ascending order
        hashmap cannot be sliced.
        use hashmap 
        '''
        records = {}
        nums = sorted(nums)
        for num in nums:
            if num in records:
                records[num] += 1
            else:
                records[num] = 1
        # print(records)
        # sort records in ascending order
        sorted_records = sorted(records.items(), key=lambda item:item[1],reverse=True)
        print(sorted_records)
        result = [pair[0] for pair in sorted_records[:k]] #practice this more.
        return result
        
        #if using minHeap, i can easily return the max 2 of the records list.
        # min heap implementations
        import heapq
        freq = {} #freq map
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])
