def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(2, isPrime(2))
print(3, isPrime(3))
print(4, isPrime(4))
print(5, isPrime(5))
print(6, isPrime(6))
print(7, isPrime(7))
print(47, isPrime(47))
print(48, isPrime(48))
