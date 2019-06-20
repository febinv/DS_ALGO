def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            queue=[]
            level=0
            max_level=0
            queue.append([root,level])
            while len(queue)>0:
                node,level=queue.pop(0)
                if level>max_level:
                    max_level=level
                if node.left:
                    queue.append([node.left,level+1])
                if node.right:
                    queue.append([node.right,level+1])
            return max_level+1