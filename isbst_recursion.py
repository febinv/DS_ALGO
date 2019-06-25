# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root,lower,upper):
            if root is None:
                return True
            if root.val <= lower or root.val>=upper:
                return False
            if not inorder(root.left,lower,root.val):
                return False
            if not inorder(root.right,root.val,upper):
                return False
            return True
            
        lower=float('-inf')
        upper=float('inf')
            
        return inorder(root,lower,upper)
        
        