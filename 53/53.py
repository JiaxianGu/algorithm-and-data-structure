def maxSubArray(nums):
    f = [0] * len(nums)
    f[0] = nums[0]
    max = 0
    for i in range(1, len(nums)):
        if f[i-1] > 0:
            f[i] = f[i-1] + nums[i]
        else:
            f[i] = nums[i]
        if f[i] > max:
            max = f[i]
    return max