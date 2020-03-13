def mergeTwoLists(l1, l2):
    # curr = dummy = ListNode(0)
    # while l1 and l2:
    #     if l1.val < l2.val:
    #         curr.next = l1
    #         l1 = l1.next
    #     else:
    #         curr.next = l2
    #         l2 = l2.next
    #     curr = curr.next
    # curr.next = l1 or l2
    # return dummy.next
    #---------------------------------
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        mergeTwoLists(l1.next, l2)
        return l1
    else:
        mergeTwoLists(l1, l2.next)
        return l2
    
