"""lst = [23, 12, 98, 43, 96, 4, 99]
lst.remove(max(lst))
print(max(lst))"""

""" n = int(input("Введите кол-во элементов: "))
l = []
for i in range(n):
    l.append(int(input(f"Введите {i+1} элемент: "))) """
""" step = 1
while step < n:
    res = []
    for i in range(0, n, step * 2):
        left = l[i:i + step]
        right = l[i + step:i + step * 2]
        a = 0
        b = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                res.append(left[a])
                a += 1
            else:
                res.append(right[b])
                b += 1
        res.extend(left[a:])
        res.extend(right[b:])
    l = res
    step *= 2
print(l) """

""" def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = []
    middle = []
    right = []
    for x in lst:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)
print(quicksort(l))

x = int(input("Введите элемент для поиска: "))
left = 0
right = len(l) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if l[mid] == x:
        print(f"Элемент {x} найден, позиция: {mid + 1}")
        found = True
        break
    elif l[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
if found == False:
    print("Элемент не найден") """

n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))
a = []
b = []
print("Введите первую матрицу:")
for i in range(n):
    r = []
    for j in range(m):
        r.append(int(input(f"Введите элемент [{i+1}][{j+1}]: ")))
    a.append(r)
print("Введите вторую матрицу:")
for i in range(n):
    r = []
    for j in range(m):
        r.append(int(input(f"Введите элемент [{i+1}][{j+1}]: ")))
    b.append(r)
s = []
d = []
for i in range(n):
    row1 = []
    row2 = []
    for j in range(m):
        row1.append(a[i][j] + b[i][j])
        row2.append(a[i][j] - b[i][j])
    s.append(row1)
    d.append(row2)
print("Сложение:")
for i in range(n):
    print(s[i])
print("Вычитание:")
for i in range(n):
    print(d[i])
if n == m:
    c = []
    for i in range(n):
        row = []
        for j in range(n):
            x = 0
            for k in range(n):
                x += a[i][k] * b[k][j]
            row.append(x)
        c.append(row)
    print("Умножение:")
    for i in range(n):
        print(c[i])
else:
    print("Умножение невозможно")
