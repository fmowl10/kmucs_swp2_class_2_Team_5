import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    if n in [0, 1]:
        return n

    i, j = 0, 1
    for _ in range(2, n + 1):
        i, j = j, i + j

    return j

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
