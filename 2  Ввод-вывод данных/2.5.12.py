#num = int(input())
#last_digit = num % 10
#first_digit = num // 10
#print('Искомое число =', last_digit * 10 + first_digit)

#Последняя цифра: (num % 101) // 100;
#Предпоследняя цифра: (num % 102) // 101;
#Предпредпоследняя цифра: (num % 103) // 102;
#.....
#Вторая цифра: (num % 10n-1) // 10n-2;
#Первая цифра: (num % 10n) // 10n-1

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')

