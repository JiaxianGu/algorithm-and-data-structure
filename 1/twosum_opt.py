class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target-nums[i]], i]
            else:
                dic[target-nums[i]] = i
        return