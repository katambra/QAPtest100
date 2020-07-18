bs = 0
def bubble_sort(a):     # сортировка пузырьком по невозрастанию через функцию
    global bs
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                bs += 1
    return a
                                                # список для примера: a = 2, 7, 3, 8, 78, 34, 67, 33, 8
a = input('Введите список:' ).split(", ") # строка ввода в список
for i in range(N):    # преобразование в список чисел
    a[i] = int(a[i])

N = len(a)

bubble_sort(a)


ins = 0
def insertion(A):      # сортировка вставками на убывание
    for i in range(1, len(A)):
        b = A[i]
        j = i - 1
        global ins
        while (j >= 0) and (b > A[j]):
            A[j+1] = A[j]
            j -= 1
            
        A[j+1] = b
        ins += 1
    return A


insertion(a)

print(f'Сортировка введенного списка методом пузырька - {bs} перестановок, методом вставок - {ins} перестановок')