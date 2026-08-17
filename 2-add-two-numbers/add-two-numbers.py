class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        m = []
        n = []
        while curr1:
            m.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            n.append(curr2.val)
            curr2 = curr2.next
        s = []
        carry = 0
        i = 0
        while i < len(m) or i < len(n):
            x = m[i] if i < len(m) else 0
            y = n[i] if i < len(n) else 0
            total = x + y + carry
            s.append(total % 10)
            carry = total // 10
            i += 1
        if carry:
            s.append(carry)
        head = ListNode(s[0])
        curr = head
        for x in s[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        return head