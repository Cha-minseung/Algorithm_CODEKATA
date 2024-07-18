num = int(input('수:'))

def Fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0

    else:
        return Fibo(n-1) + Fibo(n-2)

print(Fibo(num))