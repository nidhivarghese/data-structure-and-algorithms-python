def factorialByRecursion(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorialByRecursion(num - 1)


def factorialByIteration(num):
    fact = 1

    while num >= 2:
        fact *= num
        num -= 1

    return fact

print(factorialByRecursion(0))
print(factorialByRecursion(1))
print(factorialByRecursion(5))
print(factorialByRecursion(10))
print(factorialByRecursion(50))
print(factorialByRecursion(100))

print()

print(factorialByRecursion(0))
print(factorialByRecursion(1))
print(factorialByRecursion(5))
print(factorialByIteration(10))