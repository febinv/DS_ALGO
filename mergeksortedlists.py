# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
     def mergeKLists(self, lists):
        # write your code here
        #use minheap
        import heapq
        dummy = ListNode(0)
        head = dummy
        h = []
        for i in lists:
            if i:
                heapq.heappush(h,(i.val,i))
        while h:
            cur = heapq.heappop(h)
            head.next = cur[1]
            if cur[1].next:
                heapq.heappush(h,(cur[1].next.val,cur[1].next))
            head = head.next
        return(dummy.next)