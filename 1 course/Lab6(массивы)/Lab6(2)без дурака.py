a = list(map(int, input('Введите элементы массива: ').split()))
for i in a:
    if i < 0:
       a.remove(i) 
print('Количество отрицательных элементов: ', len(a))


