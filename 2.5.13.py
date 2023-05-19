a = int(input())
num_1 = a // 100
num_2 = (a // 10) % 10
num_3 = a % 10
ans_sum = num_1 + num_2 + num_3
ans_multpl= num_1 * num_2 * num_3

print('Сумма цифр =', ans_sum)
print('Произведение цифр =', ans_multpl)
