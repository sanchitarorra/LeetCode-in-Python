# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xdepth = 0
        self.ydepth = 0
        self.xparent = 0
        self.yparent = 0
        def dfsHelper(node, depth, parent):
            if node.left:
                dfsHelper(node.left, depth + 1, node.val)
            if node.right:
                dfsHelper(node.right, depth + 1, node.val)
            if node.val == x:
                self.xdepth = depth
                self.xparent = parent
            if node.val == y:
                self.ydepth = depth
                self.yparent = parent
        dfsHelper(root, 0, root.val)
        if self.xdepth == self.ydepth and self.xparent != self.yparent:
            return True 
        else:
            return False
            
            
                

                
                
            
        
        
            