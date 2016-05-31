#coding: utf-8
'''
Выведите разложение натурального числа n > 1 на простые множители. Простые множители должны быть упорядочены по возрастанию и разделены пробелами.

Sample Input:
75
Sample Output:
3 5 5 
'''
n = gets.to_i
exit if n==0 # все же и 0 встретился в тесте
i = 2
end_i = n/2+1
res = []

while i <= end_i
  if n % i == 0
    res<<i
    n = (n / i).to_i
  else
    i += 1
  end
end

puts res.count>0 ? res.join(' ') : n