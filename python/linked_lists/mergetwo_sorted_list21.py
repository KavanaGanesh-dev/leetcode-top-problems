'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''
 


# few insights from understanding the problem
# 1.two linked lists are sorted
# 2.create a dummy node with value =0 and keep a current pointer at the dummy node
# 3. condition1 : two list1 and list2 are not Null
    # here compare the values of list1 and list2 
    # if list1.val < list2.val; 
        # current.next should point to list1 node
        # list1 should point to list1.next
    # else:
         # current.next should point to list2 node
        # list2 should point to list2.next
    # move the curren to current.next

# 4.condition2: if list1 is present but list2 is empty
    # current.next should point to list1 node
    # list1 should point to list1.next
# 5.condition3: if list2 is present but list1 is empty
    # current.next should point to list2 node
    # list2 should point to list2.next
# 6.finally return the dummy.next

# Complexity
# Time:
# Space:


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0)
            current = dummy

            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next


            if list1 is not None:
                current.next = list1
                list1 = list1.next

            if list2 is not None:
                current.next = list2
                list2 = list2.next
                 
                 
            return dummy.next


def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)



list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

result = Solution().mergeTwoLists(list1, list2)
print_linked_list(result)
