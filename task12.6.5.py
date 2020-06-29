a = str(input())

a = a.replace(" ", "").lower()

b = a[::-1]
if a == b:
    print('палиндром')
else:
    print('это не палиндром')