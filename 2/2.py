class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers(l1, l2):
    dummy = tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        tail.next = ListNode(sum % 10)
        tail = tail.next
        carry = sum // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next