class Solution(object):
    def maximumWealth(self, accounts):
        maxi=[]
        for i in range(len(accounts)):
            maxi.append(sum(accounts[i]))
        n=max(maxi)
        return n
            