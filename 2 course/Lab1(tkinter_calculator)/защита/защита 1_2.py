from math import sqrt
from tkinter import *
root = Tk()
root.title("Вычисление нибольшего расстояния между точками")
root.geometry("250x100")

table_name = Entry(root,width = 33)
table_name.grid(row = 2, column = 0,columnspan = 3, pady = 10,padx = 20)

table_name.focus_set()
def find():
    x = []
    y = []
    a = []
    b = table_name.get()
    b = b.split(' ')
    for i in b:
        a.append(int(i))
    for i in range(0,len(a),2):
        x.append(a[i])
    for k in range(1,len(a),2):
        y.append(a[k])
##    for i in table_name.get():
##        a.append(i)
##        for i in range(len(a)):         
##            if a[i] != ' ' and a[i+1] != ' ':
##                a[i] = a[i] + a[i+1]
##            if a[i] == ' ':
##                a.pop(i)
##    print(a)
##        for i in range(0,len(a),4):
##            if a[i] != ' ' or (a[i] != 0 and a[i+1] != 0):
##                x.append(a[i])
##        for k in range(2,len(a),4):
##            if a[k] != ' ' or (a[k] != 0 and a[k+1] != 0):
##                y.append(a[k])
##    print('x',x)
##    print('y',y)
    minx = min(x)
##    print(minx)
    maxx = max(x)
##    print(maxx)
    miny = min(y)
##    print(miny)
    maxy = max(y)
##    print(maxy)
    L  = sqrt((int(maxx) - int(minx))**2 + (int(maxy) - int(miny))**2)
    messagebox.showinfo("Расстояние между наиболее удаленными точками равен = ",L)
    print(maxx, maxy, minx,  miny)









Button(text = "Перевести",command = find).grid(row = 6, column = 1, padx  = 20)

root.mainloop()

