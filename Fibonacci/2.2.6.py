'''
Задача на программирование: небольшое число Фибоначчи



Дано целое число 1≤n≤401≤n≤40, необходимо вычислить nn-е число Фибоначчи (напомним, что F0=0F0=0, F1=1F1=1 и Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 при n≥2n≥2).

Sample Input:
3
Sample Output:
2
'''
fib_arr = [0,1]

def fib(n):
    if n<len(fib_arr) :
        return fib_arr[n]
    fib_arr.append(fib(n-1)+fib(n-2))
    return fib_arr[n]

a = int(input())

print(fib(a))
