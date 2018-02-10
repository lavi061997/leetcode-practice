class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {

        }

        res = []

        for ind, val in enumerate(nums):
            diff = target - val
            if(diff not in h):
                h[val] = ind
            else:
                res.extend([ind, h[diff]])
                break

        return sorted(res)
