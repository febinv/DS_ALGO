import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.higher_minHeap=[]
        self.lowers_maxHeap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.lowers_maxHeap)==0 or num < -1*self.lowers_maxHeap[0]:
            heapq.heappush(self.lowers_maxHeap,-num)
        else:
            heapq.heappush(self.higher_minHeap,num)
                  
        if len(self.lowers_maxHeap)>len(self.higher_minHeap)+1:
            heapq.heappush(self.higher_minHeap,-heapq.heappop(self.lowers_maxHeap))
        elif len(self.higher_minHeap)>len(self.lowers_maxHeap)+1:
            heapq.heappush(self.lowers_maxHeap,-heapq.heappop(self.higher_minHeap))
    
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.higher_minHeap)==len(self.lowers_maxHeap):
            return (self.higher_minHeap[0]+-1*self.lowers_maxHeap[0])/2.0
        else:
            if len(self.higher_minHeap)>len(self.lowers_maxHeap):
                return self.higher_minHeap[0]
            else:
                return -1*self.lowers_maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
