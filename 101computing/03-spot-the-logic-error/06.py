def iterativeSum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

print(f'iterativeSum {5} - {iterativeSum(5)}')
print(f'iterativeSum {6} - {iterativeSum(6)}')