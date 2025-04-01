from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = None
        self.left = None
        self.right = None
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        '''
        Use Iteration Method, NOT recursive method.
        Using deque over queue minimize the computational overheads. 
        It can implement all the possible operations for Trees.
        '''
        
        #Member Function: check(); check if two nodes are structually, value-wise same
        def check(p: TreeNode, q: TreeNode)-> bool:
            if not p and not q: # base case: if p and q are both empty; it means it's same. empty deque
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return True
        deq = deque([(p, q)]) # (p,q) pair to compare two trees value
        while deq:
            p, q = deq.popleft()
            # if it's not OK, then return False
            if not check(p, q):
                return False
            if p and q:
                deque.append(p.left, q.left)
                deque.append(p.right, q.right)
        return True
