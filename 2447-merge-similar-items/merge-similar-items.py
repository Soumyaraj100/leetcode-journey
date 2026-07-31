class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        d = {}
        for value, weight in items1 + items2:
            d[value] = d.get(value, 0) + weight
        return sorted(d.items())
        