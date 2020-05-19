def fibo(n):
    if n <= 1:
        return 1
    else:
        return(fibo(n-1) + fibo(n-2))


num = int(input('How many Fibonacci numbers do you want? '))
print('Fibonacci sequence :', end=' ')
for i in range(num):
    print(fibo(i), end=' ')
