def maxSubArray(nums):
    max_num = max(nums)
    if max_num <= 0:
        return max_num
    else:
        max_num = nums[0]
    f = [0] * len(nums)
    f[0] = nums[0]
    max_num = nums[0]
    for i in range(1, len(nums)):
        if f[i-1] > 0:
            f[i] = f[i-1] + nums[i]
        else:
            f[i] = nums[i]
        if f[i] > max_num:
            max_num = f[i]
    return max_num


print(maxSubArray([-1,-2,-3,-4,-5]))