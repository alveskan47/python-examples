def tribonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    elif number == 3:
        return 1
    else:
        return tribonacci(number - 3) + tribonacci(number - 2) + tribonacci(number - 1)

index = int(input("Enter the index for Tribonacci > "))

print(f'Tribonacci[{index}] = {tribonacci(index)}')