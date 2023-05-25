x = int(input())
if 9999 >= x >= 999 and ( x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')