class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        i=0
        maxval=0
        minprice=float('inf')
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            elif prices[i]-minprice>maxval:
                maxval=prices[i]-minprice
        return maxval