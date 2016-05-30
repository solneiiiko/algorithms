'''
Задача на программирование: последняя цифра большого числа Фибоначчи
Дано число 1≤n≤1071≤n≤107, необходимо найти последнюю цифру nn-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи: если 0≤a,b≤90≤a,b≤9 — последние цифры чисел FiFi и Fi+1Fi+1 соответственно, то (a+b)mod10(a+b)mod10 — последняя цифра числа Fi+2Fi+2.

Sample Input:
193150
Sample Output:
5
'''

def sum(a,b):
    return (a+b)%10

def fib_last_digit(n):
    if n<2:
        return n
    old_fib = 0
    current_fib = 1
    for i in range(2,n+1):
        new_fib = sum(old_fib, current_fib)
        old_fib = current_fib
        current_fib = new_fib
    return current_fib 

a = int(input())
print(fib_last_digit(a))