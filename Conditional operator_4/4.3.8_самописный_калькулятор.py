a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif b == 0:
    print('На ноль делить нельзя!')
elif c == '/':
    print(a / b) 
else:
    print('Неверная операция')

#Более изящное решение
# a, b = int(input()), int(input())
# s = input()
# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# # elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')