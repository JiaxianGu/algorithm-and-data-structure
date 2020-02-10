def isPalindrome(x):
    a = abs(x)
    temp = 0
    result = 0
    while a != 0:
        temp = a % 10
        print('temp:', temp)
        result = result * 10 + temp
        print('result', result)
        a = a // 10
        print('a', a)
        print()
    if result == x:
        return True
    else:
        return False

print(isPalindrome(121))