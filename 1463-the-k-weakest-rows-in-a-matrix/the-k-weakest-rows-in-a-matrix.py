class Solution(object):
    def kWeakestRows(self, mat, k):
        arr = []
        for i, row in enumerate(mat):
            arr.append((sum(row), i))
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
