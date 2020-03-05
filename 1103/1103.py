def distributeCandies(candies, num_people):
    ans = [0] * num_people
    i = 0
    while candies > 0:
        if i+1 <= candies:
            ans[i % num_people] += i + 1
            candies -= i + 1
        else:
            ans[i % num_people] += candies
            candies -= candies
        i += 1
    return ans