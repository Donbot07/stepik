a = int(input())
b = int(input())
c = int(input())
num_1 = max(a, b, c)
num_3 = min(a, b, c)
num_2 = (a + b + c) - (num_1 + num_3)
print(num_1)
print(num_2)
print(num_3)