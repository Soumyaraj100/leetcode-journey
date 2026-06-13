class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        prevA = list1
        for _ in range(a - 1):
            prevA = prevA.next
        afterB = prevA
        for _ in range(b - a + 2):
            afterB = afterB.next
        prevA.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = afterB
        return list1