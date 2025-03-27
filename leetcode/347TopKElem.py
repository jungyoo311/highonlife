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
        #if using maxHeap, i can easily return the max 2 of the records list.