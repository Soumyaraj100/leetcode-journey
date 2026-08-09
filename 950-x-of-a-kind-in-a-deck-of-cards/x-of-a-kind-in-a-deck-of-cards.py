class Solution(object):
    def hasGroupsSizeX(self, deck):
        m = min(deck.count(x) for x in set(deck))
        for x in range(2, m + 1):
            ok = True
            for y in set(deck):
                if deck.count(y) % x != 0:
                    ok = False
                    break
            if ok:
                return True
        return False