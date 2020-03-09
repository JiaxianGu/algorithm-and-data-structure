def findContinuousSequence(target):
    l = 1
    r = 2
    ans = []
    while True:
        sum = (l + r) * (r - l + 1)/2
        if sum == target:
            ans.append(list(range(l, r+1)))
            l += 1

        else:
            if sum < target:
                r += 1
            else:
                l += 1
        if l >= r:
            break
    return ans
