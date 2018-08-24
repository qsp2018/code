#Given a sorted linked list, delete all duplicates such that each element appear only once.
#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if head == None:
    		return head
    	head1 = ListNode(1)
    	head1.next = head
    	current = head1.next

    	while current.next != None:
    		if current.val == current.next.val:
    			current.next = current.next.next
    			continue
    		else:
    			current = current.next

    	return head1.next
