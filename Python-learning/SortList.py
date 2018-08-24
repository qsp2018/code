# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x #x
         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def findMiddle(self,head):
        slow = head
        fast = head
        # print '-----fast:',fast, fast.val, fast.next  
        count = 0
        pre_slow = slow
        if fast.next is not None: # to get second middle if even
            fast = fast.next
            slow = slow.next
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            pre_slow = slow
            slow = slow.next
            count += 1
        pre_slow.next = None
        return slow

    def listLength(self,head):
        count = 0
        this = head
        if this == None:
            return count
        elif this != None and this.next is None:
            return 1
        while this.next is not None:
            this = this.next
            count += 1
        return count + 1

    def printAll(self,head):
        count = 0
        this = head
        if this == None:
            return 0
        while this is not None:
            print this.val
            this = this.next
        return count + 1

    def merge(self,head1,head2):
        head0 = ListNode(-1)
        #if head1.val <= head2.val:
        #    head0.next = head1
        #else:
        #    head0.next = head2
        last = head0
        while True:
            if head1.val <= head2.val:
                if head1.next is None:
                    head1.next = head2
                    last.next = head1
                    break
                else:
                    last.next = head1
                    last = head1
                    head1 = head1.next
            elif head1.val > head2.val:
                if head2.next is None:
                    head2.next = head1
                    last.next = head2
                    break
                else:
                    last.next = head2
                    last = head2
                    head2 = head2.next
        return head0.next

    def sortList(self, head):
        if head.next is None or head is None: # less or equal 1 element
            #print 'head is ', head.val
            return head
        head2 = self.findMiddle(head)
        head1 = self.sortList(head)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head





point1 =  ListNode(400)
point2 =  ListNode(100)
point3 =  ListNode(20)
point4 =  ListNode(100)
point5 =  ListNode(8)
point6 =  ListNode(800)
point7 =  ListNode(102)
point8 =  ListNode(10222)
point1.next = point2
point2.next = point3
point3.next = point4
point4.next = point5
point5.next = point6
point6.next = point7
point7.next = point8

s = Solution()
print 'Before sorting'
s.printAll(point1)
print '======'
#print point1.next.val
head = s.sortList(point1)

print 'After sorting'
s.printAll(head)
print 'success!'








