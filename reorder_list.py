# Time Complexity: O(n+m) where n and m is the number of nodes
# Space Complexity:  O(1)
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # mid is at slow

        # Reverse after mid. Prev, curr, mid
        prev = None
        curr = slow.next
        slow.next = None

        next = curr.next
        while(curr.next != None):
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        curr.next = prev

        fast = curr
        slow = head

        curr1 = head
        curr2 = curr
        
        # algo
        while(curr2!= None):
            temp1 = curr1.next
            curr1.next = curr2
            curr1 = temp1
            temp2 = curr2.next
            curr2.next = temp1
            curr2 = temp2
        return head
    