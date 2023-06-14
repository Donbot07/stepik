a = int(input())
num_1 = a // 100
num_2 = (a % 100) //10
num_3 = a % 10

num_max = max(num_1, num_2, num_3)
num_min = min(num_1, num_2, num_3)
num_mid = (num_1 + num_2 + num_3) - (num_max + num_min)
if num_mid == num_max - num_min:
    print('Число интересное')
else:
    print('Число неинтересное')