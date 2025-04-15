from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # think of the decision tree
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
            if total > target or i > len(candidates):
                return
            # to the left; includes candidates[i]
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            # to the right; excludes candidates[i]
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res