from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        '''
        member function check():
        for every node visit, check if two subtrees of every node never differs by no more than one
        True: if it's ok, balanced
        False: it's not ok, non-balanced
        '''
        def check(node):
            if not node:
                return 0
            lt = check(node.left)
            rt = check(node.right)
            if lt == -1 or rt == -1:
                return -1
            if abs(lt - rt) > 1:
                return -1
            return 1 + max(lt, rt)
        if check(root) == -1:
            return False
        return True
