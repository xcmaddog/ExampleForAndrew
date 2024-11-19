def fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return fib(num-1) + fib(num-2)

def fib2(n, prev1, prev2):
    if n < 3:
        return
    fn = prev1 + prev2
    prev2 = prev1
    prev1 = fn
    print(fn, end=" ")
    fib2(n - 1, prev1, prev2)

print(fib(16))