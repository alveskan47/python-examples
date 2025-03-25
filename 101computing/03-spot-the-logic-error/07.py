def factorial(n):
    if n == 0:
       return 1 #because 0! is 1
    else:
       f = 1
       for i in range(1,n+1):
          f = f * i
       return f

print(f'factorial {5} - {factorial(5)}')
print(f'factorial {6} - {factorial(6)}')