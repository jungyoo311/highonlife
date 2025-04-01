from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k:int) -> int:
        counter, result = 0, None
        def inorder(node):
            nonlocal counter, result
            inorder(node.left)
            counter += 1
            if counter == k:
                result = node.val
                return result # rather than returning nothing, if i return the result here, the code does not traverse the whole tree and the efficiency went high.
            inorder(node.right)
            return result
        inorder(root)
        return result
    
'''
Time Complexity: In the worst case: it will visit all nodes O(n)
In average/best case: the traversal stops once you've visited the k th smallest nodes:
O(H + K)  where H is the height of the tree
if tree is balanced: H  = log n

'''