from tkinter import *
from tkinter import messagebox
from itertools import permutations, combinations

#Оформление окна
root = Tk()
root.title("Cross")
root.geometry("350x400+450+180")
root.resizable(False, False)
root.iconbitmap("triangle.ico")

#Заголовок

head = Label(text = "Ввод данных", font = "Helvetica 20 bold")
head.grid(row = 0, column = 0, pady = 10)


a1 = Label(text = "Введите координаты точек для 1 множества"
           ,font = "consolas 8 ")
a1.grid(row = 1, column = 0, pady = 10,
        padx = 10, sticky = W)
table_name1 = Entry(root, width = 50)
table_name1.grid(row = 2, padx = 15
                 , column = 0, pady = 10, sticky = W)
table_name1.focus_set()


a2 = Label(text = "Введите координаты точек для  множества",font = "consolas 8 ")
a2.grid(row = 3, column = 0, pady = 10,
        padx = 10, sticky = W)
table_name2 = Entry(root, width = 50)
table_name2.grid(row = 4, padx = 15,
                 column = 0, pady = 10, sticky = W)


def compare(num1, num2):
    eps = 1e-7
    if abs(num1 - num2) < eps:
        return 1
    else:
        return 0


def exist(x1, y1, x2, y2, x3, y3):
    if ((compare(x1, x2) and compare(y1, y2)) or
            (compare(x1, x3) and compare(y1, y3)) or
            (compare(x2, x3) and compare(y2, y3)) or
            (compare(x1, y1) and compare(x2, y2) and compare(x3, y3)) or
            (compare(((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)), 0))):
        return 0
    else:
        return 1


def checking(x1, y1, x2, y2, x3, y3, x0, y0):
    if ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0) > 0 and
            (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0) > 0 and
            (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0) > 0):
        return True
    elif ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0) == 0 or
          (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0) == 0 or
          (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0) == 0):
        return False
    else:
        return False


def head(set1, set2):
    set1_1 = []
    set2_2 = []
    i = 0
    while i < len(set1) - 1:
        coords1 = tuple([set1[i], set1[i + 1]])
        set1_1.append(coords1)
        i += 2
    #print(set1_1)
    k = 0
    while k < len(set2) - 1:
        coords2 = tuple([set2[k], set2[k + 1]])
        set2_2.append(coords2)
        k += 2
    #print(set2_2)

    combination = [x for x in combinations(set1_1, 3)]

    for i in combination:
        saver = list(i)
        point1 = list(saver[0])
        point2 = list(saver[1])
        point3 = list(saver[2])

        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        x3 = point3[0]
        y3 = point3[1]

        if exist(x1, y1, x2, y2, x3, y3):
            count1 = 0
            count2 = 0
            for i in set2_2:
                point = list(i)
                px = point[0]
                py = point[1]
                if checking(x1, y1, x2, y2, x3, y3, px, py) == True:

                    count2 += 1
                else:
                    continue
            for j in set1_1:
                if j != saver[0] and j != saver[1] and j != saver[2]:
                    tochka = list(j)
                    px1 = tochka[0]
                    py1 = tochka[1]
                    if checking(x1, y1, x2, y2, x3,
                                y3, px1, py1) == True:
                        count1 += 1
                    else:
                        continue

                if count1 == count2 and count1 >= 1 and count2 >= 1:
                    return -1
                    break

                else:
                    continue


def main(set1, set2):
    set1_1 = []
    set2_2 = []
    i = 0
    while i < len(set1) - 1:
        coords1 = tuple([set1[i], set1[i + 1]])
        set1_1.append(coords1)
        i += 2
    #print(set1_1)
    k = 0
    while k < len(set2) - 1:
        coords2 = tuple([set2[k], set2[k + 1]])
        set2_2.append(coords2)
        k += 2
    #print(set2_2)

    combination = [x for x in combinations(set1_1, 3)]

    for i in combination:
        saver = list(i)
        point1 = list(saver[0])
        point2 = list(saver[1])
        point3 = list(saver[2])

        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        x3 = point3[0]
        y3 = point3[1]

        if exist(x1, y1, x2, y2, x3, y3):
            count1 = 0
            count2 = 0
            for i in set2_2:
                point = list(i)
                px = point[0]
                py = point[1]
                if checking(x1, y1, x2, y2, x3, y3, px, py) == True:

                    count2 += 1
                else:
                    continue
            for j in set1_1:
                if j != saver[0] and j != saver[1] and j != saver[2]:
                    tochka = list(j)
                    px1 = tochka[0]
                    py1 = tochka[1]
                    if checking(x1, y1, x2, y2, x3,
                                y3, px1, py1) == True:
                        count1 += 1
                    else:
                        continue

                if count1 == count2 and count1 >= 1 and count2 >= 1:
                    return x1, y1, x2, y2, x3, y3
                    break

                else:
                    continue


def graph(set1, set2):
    x = []
    xx = []
    y = []
    yy = []
    for i in range(len(set1)):
        if i % 2 == 0:
            x.append(set1[i])
        else:
            y.append(set1[i])
    for k in range(len(set2)):
        if k % 2 == 0:
            xx.append(set2[k])
        else:
            yy.append(set2[k])
    if head(set1, set2) == -1:

        x1, y1, x2, y2, x3, y3 = main(set1, set2)

        root = Tk()

        root.resizable(False, False)
        canv = Canvas(root, width=1000, height=600, bg="lightblue", cursor="pencil")
        canv.create_polygon(((x1 * 20) + 500, 300 - (y1 * 20))
                            , ((x2 * 20) + 500, 300 - (y2 * 20)),
                            ((x3 * 20) + 500, 300 - (y3 * 20))
                            , fill="lightgreen", outline="black", width=2)
        canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
        canv.create_line(0, 300, 1000, 300, width=2, arrow=LAST)
        for i in range(len(x)):
            canv.create_oval(x[i] * 20 + 500, 300 - y[i] * 20
                             , x[i] * 20 + 501, 301 - y[i] * 20
                             , width=5, outline="red")
        for i in range(len(xx)):
            canv.create_oval(xx[i] * 20 + 500, 300 - yy[i] * 20
                             , xx[i] * 20 + 501
                             , 301 - yy[i] * 20, width=5,
                             outline="orange")
        start = -500
        m = -24
        p = 25
        for i in range(40000):
            if i % 800 == 0:
                n = start + (1 / 40) * i
                canv.create_line(n + 500, -3 + 300
                                 , n + 500, 3 + 300
                                 , width=0.5, fill='black')
                canv.create_text(n + 515, -10 + 300
                                 , text=str(m), fill="purple"
                                 , font=("Helvectica", "5"))
                m += 1
                if (n != 0):
                    canv.create_line(-3 + 500, n + 300
                                     , 3 + 500, n + 300
                                     , width=0.5, fill='black')
                    canv.create_text(20 + 500, n + 300
                                     , text=str(p), fill="purple"
                                     , font=("Helvectica", "5"))
                    p -= 1

        canv.pack()
        root.mainloop()
    else:
        root = Tk()

        root.resizable(False, False)
        canv = Canvas(root, width=1000, height=600, bg="lightblue", cursor="pencil")
        canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
        canv.create_line(0, 300, 1000, 300, width=2, arrow=LAST)
        for i in range(len(x)):
            canv.create_oval(x[i] * 20 + 500
                             , 300 - y[i] * 20, x[i] * 20 + 501
                             , 301 - y[i] * 20, width=5, outline="red")
        for i in range(len(xx)):
            canv.create_oval(xx[i] * 20 + 500
                             , 300 - yy[i] * 20, xx[i] * 20 + 501
                             , 301 - yy[i] * 20, width=5,
                             outline="orange")
        start = -500
        m = -24
        p = 25
        for i in range(40000):
            if i % 800 == 0:
                n = start + (1 / 40) * i
                canv.create_line(n + 500
                                 , -3 + 300, n + 500, 3 + 300
                                 , width=0.5, fill='black')
                canv.create_text(n + 515, -10 + 300, text=str(m)
                                 , fill="purple", font=("Helvectica", "5"))
                m += 1
                if (n != 0):
                    canv.create_line(-3 + 500, n + 300
                                     , 3 + 500, n + 300
                                     , width=0.5, fill='black')
                    canv.create_text(20 + 500
                                     , n + 300, text=str(p)
                                     , fill="purple", font=("Helvectica", "5"))
                    p -= 1

        canv.pack()

        root.mainloop()


def check(key):
    if key == "Вычислить":
        count = 0
        s11 = []
        s22 = []
        set1 = (table_name1.get()).split()
        #print("s1 ", set1)
        set2 = (table_name2.get()).split()
        #print("s2 ", set2)
        if (len(set1) > 0 and len(set2) > 0):
            n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"}
            for i in set1:
                a = set(i)
                if i.isalpha() == True or a.issubset(n) == False:
                    messagebox.showerror("Ошибка!"
                                         , "Введены недопустимые символы для первого множества точек")
                    table_name1.delete(0, END)
                    table_name1.focus_set()
                    break
                else:
                    count += 1

            for i in set2:
                a = set(i)
                if i.isalpha() == True or a.issubset(n) == False:
                    messagebox.showerror("Ошибка!"
                                         , "Введены недопустимые символы для второго множества точек")
                    table_name2.delete(0, END)
                    table_name2.focus_set()
                    break
                else:
                    count += 1
            if (len(set1) % 2 == 1 ):
                messagebox.showerror("Ошибка!"
                                     , "Введены недостаточное количество пар точек для первого множества")
                table_name1.delete(0, END)
                table_name1.focus_set()
            else:
                count += 1
            if (len(set2) % 2 == 1):
                messagebox.showerror("Ошибка!"
                                     , "Введены недостаточное количество пар точек для второго множества")
                table_name2.delete(0, END)
                table_name2.focus_set()
            else:
                count += 1
            #print("count ", count)

            if count == len(set1) + len(set2) + 2:
                for i in set1:
                    s11.append(int(i))
                for j in set2:
                    s22.append(int(j))
                #print("s11 ", s11)
                #print("s22 ", s22)
                graph(s11, s22)

        else:
            messagebox.showerror("Ошибка!"
                                 , "Введено недостаточное количество входных параметров")

    if key == "Справка":
        messagebox.showinfo("Справка",
                            "Это приложение разработано для нахождения треугольника,"
                            "в котором одинаковое количество точек из первого и второго множества.\n"
                            "\nСоздал это приложение Турсунов Жасурбек, студент группы ИУ7-26Б")

    if key == "Очистить первое поле ввода":
        table_name1.delete(0, END)
    if key == "Очистить второе поле ввода":
        table_name2.delete(0, END)
    if key == "Очистить все поля":
        table_name1.delete(0, END)
        table_name2.delete(0, END)





#Лямбда функции
# Для очистки
clean1 = lambda x = "Очистить первое поле ввода": check(x)
clean2 = lambda x = "Очистить второе поле ввода": check(x)
clean5 = lambda x = "Очистить все поля": check(x)

#для вычисления
show_graph = lambda x = "Вычислить": check(x)

#для справки
info = lambda x = "Справка": check(x)



#Верхнее меню
mainmenu = Menu(root)
root.config(menu = mainmenu)

usermenu = Menu(mainmenu, tearoff = 0)
usermenu.add_command(label = "Вычислить", command = show_graph)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Очистить первое поле ввода", command = clean1)
filemenu.add_command(label = "Очистить второе поле ввода", command = clean2)
filemenu.add_command(label = "Очистить все поля", command = clean5)

mainmenu.add_cascade(label = "Действия", menu = usermenu)
mainmenu.add_cascade(label = "Очистить", menu = filemenu)
mainmenu.add_command(label = "Справка", command = info)


#Кнопка Построить график
button2 = Button(text = "Вычислить", width = 20, height = 2, font = "consolas 10 bold",bg="white",fg="#000080", command = show_graph)
button2.grid(row = 5, column = 0, pady = 20)

root.mainloop()
