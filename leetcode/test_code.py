import pytest
from n125ValidPalindrome import Solution

@pytest.mark.parametrize("input_list, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
])
def test(input_list, expected):
    sol = Solution()
    assert sol.isPalindrome(input_list) == expected