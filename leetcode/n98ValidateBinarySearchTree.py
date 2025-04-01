class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]):
        '''
        use min/max boundary implementations.
        member function check(): 
        returns the subTree recursively.
        '''
        def check(node, low, high):
            if not node: # it reached the end. 
                return True
            if not low < node.val < high: # filtering out all the edge cases
                return False
            return(
                check(node.left, low, node.val) and 
                check(node.right, node.val, high)
            )
        return check(root, float('-inf'), float('inf'))
