class Solution(object):
    def nextGreatestLetter(self, letters, target):
        ans = ""
        for x in letters:
            if x > target:
                ans = x
                break
        if ans == "":
            return letters[0]
        return ans