from typing import Optional
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def print_list(self):
        ptr = self
        while ptr:
            print(ptr.val, end=" -> ")
            ptr = ptr.next


# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 or not l2:
        return l1 if l1 else l2

    root = ListNode()
    merge = root

    # iterate through each until all nodes have been visited
    while l1 or l2:
        if l1 and l2:
            merge.next = l1 if l1.val < l2.val else l2
            if merge.next == l1:
                l1 = l1.next
            else:
                l2 = l2.next
        else:
            merge.next = l1 if l1 else l2
            if l1:
                l1 = l1.next
            else:
                l2 = l2.next
        merge = merge.next
    return root.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
head = merge_two_lists(list1, list2)
head.print_list()

