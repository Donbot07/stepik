num =int(input())

sum = (num // 100 % 10) + (num // 10 % 10)
subtr = (num // 1000 % 10) - (num % 10)
if sum == subtr:
    print('ДА')
else:
    print('НЕТ')