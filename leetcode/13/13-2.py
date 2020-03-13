def romanToInteger(s):
    table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    previous = 0
    result = 0
    for current in s:
        result += table[current]
        if previous and table[current] > table[previous]:
            result -= 2 * table[previous]
        previous = current
    return result
