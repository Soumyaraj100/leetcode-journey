# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        s = 0
        if root.left and not root.left.left and not root.left.right:
            s += root.left.val
        l = self.sumOfLeftLeaves(root.left)
        r = self.sumOfLeftLeaves(root.right)
        return s + l + r