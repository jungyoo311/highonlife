from typing import Optional, List
import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root])
        output = []
        if root is None:
            return []
        while dq:
            levelOrder = []
            qlen = len(dq)
            for i in range(qlen):
                node = dq.popleft()
                levelOrder.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            output.append(levelOrder)
        return output