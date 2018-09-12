import time


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def interfibo(n):
    if n <= 1:
        return n
    num_0 = 0
    num_1 = 1
    for i in range(0, n-1):
        num_1 = num_0 + num_1
        num_0 = num_1 - num_0
    return num_1



while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = interfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber,ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber,ts))