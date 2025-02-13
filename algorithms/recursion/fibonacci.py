def fibonacciByRecursion(num):
    if num <= 0:
        return 'Invalid Input'
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib = fibonacciByRecursion(num - 1)
        fib.append(fib[-1] + fib[-2])
        return fib


def fibonacciByIteration(num):
    fib = [0, 1]

    if num <= 0:
        return "Invalid Input"
    elif num == 1:
        return [0]
    elif num == 2:
        return fib
    else:
        for i in range(2, num):
            fib.append(fib[-1] + fib[-2])

        return fib


print(fibonacciByRecursion(10))
print(fibonacciByIteration(10))
