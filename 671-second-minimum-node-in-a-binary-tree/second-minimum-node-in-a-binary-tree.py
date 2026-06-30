class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    def findSecondMinimumValue(self, root):
        x = sorted(set(self.preorder(root)))
        if len(x) < 2:
            return -1
        return x[1]