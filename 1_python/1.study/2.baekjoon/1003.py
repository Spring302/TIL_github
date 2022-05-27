zero_count = 0
one_count = 0

def fibonacci(n):
    global zero_count, one_count
    if n==0:
        zero_count += 1
        return 0
    elif n==1:
        one_count += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())

for i in range(T):
    n = int(input())
    fibonacci(n)
    print(zero_count, one_count)
    zero_count, one_count = 0, 0