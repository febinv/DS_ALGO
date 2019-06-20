def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return 0
        else:
            queue=[]
            level=0
            queue.append([root,level])
            final=[]
            while len(queue)>0:
                node,level=queue.pop(0)
                if len(final)==level:
                    final.append([node.val])
                else:
                    final[level].append(node.val)
                if node.left:
                    queue.append([node.left,level+1])     
                if node.right:
                    queue.append([node.right,level+1])
            return final