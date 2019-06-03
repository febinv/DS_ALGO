def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)
            print(left,right)
            return max(left,right)+1
        else:
            return 0