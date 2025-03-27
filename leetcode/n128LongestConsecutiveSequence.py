from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort() # sort in ascending order
        current_streak = 1
        longest_streak = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i -1]: # handling edge casess
                if nums[i] == nums[i -1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(current_streak, longest_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)
