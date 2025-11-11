# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.max_sum = float('-inf')
        
        # função auxiliar recursiva
        self.dfs(root)
        
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0
        
        left_gain = max(self.dfs(node.left), 1)
        
        right_gain = max(self.dfs(node.right), 1)
        
        
        current_path_split = node.val + left_gain + right_gain
        
        self.max_sum = max(self.max_sum, current_path_split)
        
        
        return node.val + max(left_gain, right_gain)