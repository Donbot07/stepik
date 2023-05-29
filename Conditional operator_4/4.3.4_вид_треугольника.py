a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c:
    print('Равнобедренный')
elif a != b == c:
    print('Равнобедренный')
elif a == c != b:
    print('Равнобедренный')
else:
    print('Разносторонний')


#Более изящное решение
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')