
num = int(input("Enter a number to check for prime factors: "))


factors = []
divisor = 2

while num > 1:
    if num % divisor == 0:
        factors.append(divisor)
        num /= divisor
    else:
        divisor += 1


print(f"The prime factors of {num} are {factors}")
