a = int(input())
b = int(input())
c = int(input())
if b > a > c or b < a < c :
    print(a)
elif a > b > c or a < b < c :
    print(b)
else:
    print(c)

# elif a > b < c:
#     print(b)
# elif a > c < b:
#     print(c)