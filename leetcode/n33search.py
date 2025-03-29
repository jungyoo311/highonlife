from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid #return the idx not the value.
            elif target < nums[mid]:
                return binarySearch(left, mid -1)
            else:
                return binarySearch(mid +1, right)
        n = len(nums) # watch out of bounds
        left, right = 0, len(nums) -1
        # find the pivot index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid -1
        pivot = left
        # Decide which subarry to binary search
        if target >= nums[pivot] and target <= nums[-1]:
            return binarySearch(pivot, n -1)
        else:
            return binarySearch(0, pivot -1)