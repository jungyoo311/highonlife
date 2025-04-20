from typing import Optional
# Definition of Singly Linked-List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1->2->3->4->5
        '''
        expected: 1->5->2->4->3

        Step 1: find mid point
        Step 2: reverse 2nd LL
        Step 3: merge two spilted LL

        1->2

        4->3


        1->5->2->4->3
        
        1->2->3->4->5
        iter 1:
        head: 1
        slow: 2
        fast: 3

        iter 2:
        head: 
        slow: 3
        fast: 5
        modify head in-place instead
        '''
        # two ptr method to find the mid point.
        fast, slow = head, head
        while fast and fast.next:
            # 1->2->3->4->5
            # 1->2->3
            # 5->4
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        prev = None
        # step 2: reverse the second LL
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # step 3: merge two halves
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
