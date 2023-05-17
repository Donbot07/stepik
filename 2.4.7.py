# f(a,b) =3 (a + b) ** 3 + 275b ** 2 − 127a − 41
a = int(input())
b = int(input())
num_a = a + b
num_a = (num_a ** 3) * 3
num_b = b ** 2
num_b = 275 * num_b
num_c = 127 * a
print(num_a + num_b - num_c - 41 )
