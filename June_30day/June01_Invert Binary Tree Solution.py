    # recursive Time= O(n) space = O(d),d=depth
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    #iterative Sol Time = O(n), space = O(n)
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while len(queue) > 0:
            current = queue.pop(0)
            if current is None:
                continue
            current.left, current.right = current.right, current.left
            queue.append(current.left)
            queue.append(current.right)
        return root
        