a = (input())
b = (input())

if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный' :
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный' :
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий' :
    print('зеленый')
elif a == 'синий' == b :
    print('синий')
elif a == 'желтый' == b :
    print('желтый')
elif a == 'красный' == b :
    print('красный')
else:
    print('ошибка цвета')

# Более лучшее решение
# 
# a, b = input(), input()

# if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
#     print('зеленый')
# elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
#     print(a)
# else:
#     print('ошибка цвета')
    