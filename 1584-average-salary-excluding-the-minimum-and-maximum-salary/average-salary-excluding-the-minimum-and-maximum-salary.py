class Solution(object):
    def average(self, salary):
        total = sum(salary)
        total -= min(salary)
        total -= max(salary)
        return float(total) / (len(salary) - 2)