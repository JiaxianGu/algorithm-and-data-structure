'''
reverse digits of a 32 bit signed integer. If the reversed interger overflows, return 0
'''

def reverse(x):
    a = abs(x)
    temp = 0
    num = 0
    while a != 0:
        temp = a % 10
        num = num * 10 + temp
        a = a // 10
    '''
    -2147483648~2147483647
    '''
    if  x > 0 and num < 2147483648:
        return num
    elif x < 0 and num < 2147483649:
        return -(num)
    else:
        return 0