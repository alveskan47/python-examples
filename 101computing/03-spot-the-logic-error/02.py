def findMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(findMax(7, 3, 9))
print(findMax(7, 9, 3))
print(findMax(9, 7, 3))
print(findMax(9, 3, 7))
print(findMax(3, 9, 7))
print(findMax(3, 7, 9))
