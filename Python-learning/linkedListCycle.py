# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	h1 = head
    	h2 = head
    	while True:
	    	if h1 == None or h2 == None:
	    		return False
	    	elif h2.next == None:
	    		return False	    	
	    	h1 = h1.next
	    	h2 = h2.next.next
	    	if h1 is h2:
	    		return True
	    	


        