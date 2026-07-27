class Solution(object):
    def averageOfSubtree(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            total = ls + rs + node.val
            cnt = lc + rc + 1
            if total // cnt == node.val:
                self.ans += 1
            return (total, cnt)
        dfs(root)
        return self.ans