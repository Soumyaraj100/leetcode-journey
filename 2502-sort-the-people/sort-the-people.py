class Solution(object):
    def sortPeople(self, names, heights):
        s = list(zip(names, heights))
        s.sort(key=lambda x: x[1], reverse=True)
        c = []
        for x, y in s:
            c.append(x)
        return c