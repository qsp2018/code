# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printAll(self,head):
        count = 0
        this = head
        if this == None:
            return 0
        while this is not None:
            print this.val
            this = this.next
        return count + 1

    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        
        if not isinstance(head, ListNode):
             print "no type"
             return 
             #sys.exit(-1)


        head0 = ListNode(-1)
        head0.next = head
        second = head.next
        head.next = None
        
        first = head
        first_last = head0



        while second is not None:   
            first_last = head0
            first = first_last.next
            while first is not None:
                if second.val < first.val:
                    first_last.next = second
                    keep = second.next
                    second.next = first
                    second = keep
                    print '--'
                    self.printAll(head0)
                    print '---'
                    self.printAll(second)
                    print '----'                    
                    break
                
                if first.next is None:
                    first.next = second
                    keep = second.next
                    second.next = None
                    second = keep
                    break
                first_last = first
                first = first.next
        return head0.next


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
head = s.insertionSortList('')

print 'After sorting'
s.printAll(head)
print 'success!'
