import heapq
import collections
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count=collections.Counter(nums)
    heap=[]
    for word,freq in count.items():
        heap.append((-freq,word))
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


print(topKFrequent([1,1,1,2,2,3],2))