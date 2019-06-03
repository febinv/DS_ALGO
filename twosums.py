    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check={}
        for i in range(len(nums)):
            if target-nums[i] in check:
                return [check[(target-nums[i])],i]
            if nums[i] not in check:
                check[nums[i]]=i
            