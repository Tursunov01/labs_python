n = int(input("Input size of list: "))
a = []
for i in range(n):
    number = int(input("Input element of list: "))
    a.append(number)

#сортировка шейкером
def shaker_Sort(a): 
    #l, r границы неотсортированной части массива
    k = r = len(a)-1
    l = 1
    while ( l < r ):
        # проход справо налево 
        for j in range (r, l-1, -1):
            if a[j-1] > a[j]: 
                a[j-1], a[j] = a[j], a[j-1]
                k = j
            l = k
        # проход слева направо 
        for j in range (l, r + 1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                k = j
            r = k
    return a
print()
print("Sorted array is ", shaker_Sort(a)) 
    
