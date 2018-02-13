class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        res = []

        for i in range(0,len(nums)):
            res.append(prod)
            prod = prod * nums[i]
        prod = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * prod
            prod = prod * nums[i]

        return res
