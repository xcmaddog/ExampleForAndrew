def fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 1
    return fib(num-1) + fib(num-2)

print(fib(16))