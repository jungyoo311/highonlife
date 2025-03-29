from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
        '''
        Step1: Traverse and print all the nodes
        Step 2: Swap left to right, right to left
        left -> right
        right -> left

        Question: How can i figure out level of the tree.
            ANS: Use DFS to find the end. as it goes down increment level counter.
        adjacency matrix? NO

        Current Bottleneck: if it's LL, i can do curr = curr.next. 
        But it's Tree so i don't know how to backtrack once it reached the end of left subtree.

        No need to traverse using BFS. I was bascially tried to implement BFS from scratch here.
        '''