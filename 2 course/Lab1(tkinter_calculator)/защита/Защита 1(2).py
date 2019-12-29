from tkinter import *
import math

root = Tk()
root.title("Вычисление нибольшего расстояния между точками")
root.geometry("250x120")

table_name = Entry(root,width = 33)
table_name.grid(row = 2, column = 0,columnspan = 3, pady = 10,padx = 20)


table_print = Entry(root,width = 33)
table_print.grid(row = 4, column = 0,columnspan = 3, pady = 10,padx = 20)

table_name.focus_set()
def choice():
    a = (table_name.get())
    massiv = a.split() # для хранения всех координат без пробела
    distance = [] #  для хранения расстояния
    for i in range (len(massiv)):
        massiv[i] = int(massiv[i])
    numbers1 = [] # для хранения  названия точек
    numbers2 = [] # для хранения названия точек
    for i in range(0,len(massiv), 2):
        for j in range(i+2,len(massiv),2):
            rasstoyanie = math.sqrt(((massiv[j] - massiv[i])**2) + ((massiv[j+1] - massiv[i+1])**2))
            rasstoyanie = round(rasstoyanie,3)
            distance.append(rasstoyanie)
            numbers1.append(j/2)
            numbers2.append(i/2)



    maxras = distance[0]
    position = 0
    for i in range (len(distance)):   # нахожу максимальное расстояние
        if (distance[i] > maxras):
            maxras = distance[i]
            position = i

    
    table_print.insert(END, str((str(int(numbers1[position]+1)) + '  и  '+ str(int(numbers2[position]+1)))))


Button(text = "Перевести",command = choice).grid(row = 6, column = 1, padx  = 20)

root.mainloop()

