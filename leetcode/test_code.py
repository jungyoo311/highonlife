import pytest
from n128LongestConsecutiveSequence import Solution

@pytest.mark.parametrize("input_list, expected", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,0,1,2], 3),
    ([], 0)
])
def test(input_list, expected):
    sol = Solution()
    assert sol.longestConsecutive(input_list) == expected