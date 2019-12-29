import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from math import sin, cos

#Оформление окна
root = Tk()
root.title("Cross")
root.geometry("500x400+450+180")
root.resizable(False, False)
root.iconbitmap("graph.ico")

#Заголовок

head = Label(text = "Ввод данных", font = "Helvetica 20 bold")
head.grid(row = 0, column = 0, pady = 10)


a1 = Label(text = "Введите начальную и конечную границу графика",font = "consolas 8 ")
a1.grid(row = 1, column = 0, pady = 10, padx = 5, sticky = W)
table_name1 = Entry(root, width = 30)
table_name1.grid(row = 2, padx = 10, column = 0, pady = 10, sticky = W)
table_name1.focus_set()


a2 = Label(text = "Введите шаг",font = "consolas 8 ")
a2.grid(row = 3, column = 0, pady = 10, padx = 5, sticky = W)
table_name2 = Entry(root, width = 30)
table_name2.grid(row = 4, padx = 10, column = 0, pady = 10, sticky = W)


a2 = Label(text = "Введите точность",font = "consolas 8 ")
a2.grid(row = 5, column = 0, pady = 10, padx = 5, sticky = W)
table_name3 = Entry(root, width = 30)
table_name3.grid(row = 6, padx = 10, column = 0, pady = 10, sticky = W)


a2 = Label(text = "Введите максимальное количество итераций",font = "consolas 8 ")
a2.grid(row = 7, column = 0, pady = 10, padx = 5, sticky = W)
table_name4 = Entry(root, width = 30)
table_name4.grid(row = 8, padx = 10, column = 0, pady = 10, sticky = W)

def close(window):
    window.destroy()

def f(x):
    #return x*x*x -3*x*x -5*x -1
    #return cos(x)
    #return sin(x)
    return x*x-4

def f_name():
    #return "x*x - 6*x + 7"
    return "sin(x)"


def MPD(f,a, b, eps, k):
    y1 = f(a)
    y2 = f(b)
    if y1 * y2 > 0:
        code = 2
        x = "-"
        n = "-"
        start = "a-"
        konec = "b-"
        return code, x, n, start, konec
    else:
        x = a - ((f(a) * (b-a)) / (f(b) - f(a)))
        n_1 = a
        k_1 = b
        y3 = f(x)
        n = 1
        while (abs(y3) > eps):
            x = a - (f(a) * (b-a)) / (f(b) - f(a))
            y3 = f(x)
            if y1 * y3 < 0:
                b = x
            else:
                a = x
            n += 1
        if k >= n:
            code = 0
            return(code, x, n,n_1,k_1)
        else:
            code = 1
            return (code, x, n, n_1,k_1)

def prk(a,b,n,eps, number):
    znachenie = []
    codes = []
    korni = []
    iterat = []
    nachalo = []
    konec = []
    step = int((b - a) / n)
    #print(step)
    for i in range(step):
        start = a + n *(i)
        #print(start)
        end = a + n *(i + 1)
        #print(end)
        code, x, k, a_1, a_2 = MPD(f,start,end,eps,number)
        if code == 1 or code == 0:
            codes.append(code)
        if x != "-":
            korni.append(x)
            znachenie.append(f(x))
        if k != "-":
            iterat.append(k)
        if a_1 != "a-":
            nachalo.append(a_1)
        if a_2 != "b-":
            konec.append(a_2)
    '''endd = b % n
    print(endd)
    ends = b - endd
    print(ends)'''
    code, x, k, a_1, a_2 = MPD(f,end,b,eps,number)
    if code == 1 or code == 0:
        codes.append(code)
    if x != "-":
        korni.append(x)
        znachenie.append(f(x))
    if k != "-":
        iterat.append(k)
    if a_1 != "a-":
        nachalo.append(a_1)
    if a_2 != "b-":
        konec.append(a_2)
    
    for i in range(len(korni) -2):
        if korni[i] == korni[i+1]:
            j = i
            korni.remove(korni[i])
        else:
            j = "-"
        for i in range(len(codes)):
            if i == j:
                codes.remove(codes[i])
        for i in range(len(znachenie)):
            if i == j:
                znachenie.remove(znachenie[i])
        for i in range(len(iterat)):
            if i == j:
                iterat.remove(iterat[i])
        for i in range(len(nachalo)):
            if i == j:
                nachalo.remove(nachalo[i])
        for i in range(len(konec)):
            if i == j:
                konec.remove(konec[i])
    return nachalo, konec, korni, znachenie, iterat, codes

def table(nachalo, konec, korni, znachenie, iterat, codes):
    root_table = Tk()
    root_table.geometry('+710+200')
    root_table.title("Таблица")
    '''i=0
    while i < (len(func_range)):
        if func_range[i] == 1:
            s=values.pop(i)
            s=answer.pop(i)
            s=error.pop(i)
            s=counter.pop(i)
            s =func_range.pop(i)
            i -= 1
        i += 1

    i = 0'''
    if len(korni) == 0:
        messagebox.showinfo("Вывод", "На введённом интервале нет корней.")
        close(root_table)
    else:
        height = len(korni) + 1
        width = 6
        for i in range(height):
            for j in range(width):
                if i == 0:
                    if j == 0:
                        b = Label(root_table, text=" № ")
                    elif j == 1:
                        b = Label(root_table, text=" Интервал ")
                    elif j == 2:
                        b = Label(root_table, text=" Корень ")
                    elif j == 3:
                        b = Label(root_table, text=" Функция от корня ")
                    elif j == 4:
                        b = Label(root_table, text=" Кол-во итераций ")
                    elif j == 5:
                        b = Label(root_table, text=" Ошибка ")
                else:
                    if j == 0:
                        b = Label(root_table, text = str(i))
                    elif j == 1:
                        a1 = nachalo[i - 1]
                        b1 = konec[i - 1]
                        c1 = "[" + str(a1) + ":" + str(b1) + "]"
                        b = Label(root_table, text = c1)
                    elif j == 2:
                        a2 = "{:1.2e}".format(korni[i - 1])
                        b = Label(root_table, text = a2)
                    elif j == 3:
                        a3 = "{:.0e}".format(znachenie[i - 1])
                        b = Label(root_table, text = a3)
                    elif j == 4:
                        b = Label(root_table, text = iterat[i-1])
                    elif j == 5:
                        b = Label(root_table, text = codes[i-1])
                b.grid(row=i, column=j)

    '''b1 = Label(root_table, text="Код ошибки:")
    b2 = Label(root_table, text=' "0" - корень успешно найден')
    b3 = Label(root_table, text=' "1" - за ' + str(n) + ' итерации(й) корень не был найден')
    b4 = Label(root_table, text=' "2" - невозможно вычислить корень данным методом')

    b1.grid(row=len(error) + 2, column=0, columnspan=3)
    b2.grid(row=len(error) + 3, column=0, columnspan=3)
    b3.grid(row=len(error) + 4, column=0, columnspan=3)
    b4.grid(row=len(error) + 5, column=0, columnspan=3)

    make_grafik(start, end)'''

    mainloop()


def graph(start, end, eps,step):
    stepp = 0.001
    if abs(f(start)) < eps:
        start -= 1
    if abs(f(end)) < eps:
        end += 1
    endd = end % step
    konec = end - endd
    x = np.arange(start, end, stepp)
    y = []
    for i in x:
        y.append(f(i))

    fig = plt.figure()
    plt.plot(x, y)  # ломаная линия;

    for i in x:
        if f(i - 0.01) < f(i) and f(i + 0.01) < f(i) \
                or f(i - 0.01) > f(i) and f(i + 0.01) > f(i):
            plt.scatter(i, f(i), c='red')  # маркер или точечное рисование (экстремумы);

        elif (abs(f(i)) <= 0.01):
            plt.scatter(i, f(i), c='g') #f(i)

    # text1 = plt.text(1.5, 1.5, 'Red - экстремумы\n Green - корни')
    plt.title('Function graph ' + f_name() + '\nRed - extremums\n' + 'Green - korni')

    # Название координатных осей
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.axhline(0, color="black", linestyle="--")
    plt.axvline(0, color="black", linestyle="--")
    plt.grid()  # Линии вспомогательной сетки
    plt.show()

def check(key):
    if key == "Найти корни":
##        table_name1.config(state = NORMAL)
##        table_name2.config(state = NORMAL)
##        table_name3.config(state = NORMAL)
##        table_name4.config(state = NORMAL)
        count = 0
        edges = (table_name1.get()).split()
        step = table_name2.get()
        step1 = (table_name2.get()).split()
        step_set = set(step)
        eps = table_name3.get()
        eps1 = (table_name3.get()).split()
        eps_set = set(eps)
        number_of_iterations = table_name4.get()
        number_of_iterations1 = (table_name4.get()).split()
        number_of_iterations_set = set(number_of_iterations)
        if (len(edges) == 2 and len(step1) == 1 and len(eps1) == 1 and len(number_of_iterations1) == 1):
            n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "e", "."}
            for i in edges:
                a = set(i)
                if i.isalpha() == True or a.issubset(n) == False:
                    messagebox.showerror("Ошибка!", "Введены недопустимые символы для границы")
                    table_name1.delete(0, END)
                    table_name1.focus_set()
                    break
                else:
                    count += 1
            if step.isalpha() == True or step_set.issubset(n) == False or float(step) < 0:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для шага")
                table_name2.delete(0, END)
                table_name2.focus_set()
            else:
                count += 1
            if eps.isalpha() == True or eps_set.issubset(n) == False:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для точности")
                table_name3.delete(0, END)
                table_name3.focus_set()
            else:
                count += 1
            if number_of_iterations.isalpha() == True or number_of_iterations_set.issubset(n) == False or float(number_of_iterations) < 0:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для итераций")
                table_name4.delete(0, END)
                table_name4.focus_set()
            else:
                count += 1
            if (float(edges[1]) - float(edges[0])) < float(step):
                messagebox.showerror("Ошибка!", "Введенный шаг больше введенного интервала")
                table_name1.delete(0, END)
                table_name2.delete(0, END)
                table_name1.focus_set()
            else:
                count += 1
            if count == 6:
                '''table_name1.config(state="readonly")
                table_name2.config(state="readonly")
                table_name3.config(state="readonly")
                table_name4.config(state="readonly")'''
                nachalo, konec, korni, value, iterations, code_of_error = prk(float(edges[0]), float(edges[1]),
                                                                              float(step), float(eps),
                                                                              int(number_of_iterations))
                table(nachalo, konec, korni, value, iterations, code_of_error)



        else:
            messagebox.showerror("Ошибка!", "Введено недостаточное количество вхлдных параметров")
            '''table_name1.delete(0, END)
            table_name2.delete(0, END)
            table_name3.delete(0, END)
            table_name4.delete(0, END)
            table_name1.focus_set()'''

    if key == "Построить график":
##        table_name1.config(state=NORMAL)
##        table_name2.config(state=NORMAL)
##        table_name3.config(state=NORMAL)
##        table_name4.config(state=NORMAL)
        count = 0
        edges = (table_name1.get()).split()
        step = table_name2.get()
        step1 = (table_name2.get()).split()
        step_set = set(step)
        eps = table_name3.get()
        eps1 = (table_name3.get()).split()
        eps_set = set(eps)
        number_of_iterations = table_name4.get()
        number_of_iterations1 = (table_name4.get()).split()
        number_of_iterations_set = set(number_of_iterations)
        if (len(edges) == 2 and len(step1) == 1 and len(eps1) == 1 and len(number_of_iterations1) == 1):
            n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "e", "."}
            for i in edges:
                a = set(i)
                if i.isalpha() == True or a.issubset(n) == False:
                    messagebox.showerror("Ошибка!", "Введены недопустимые символы для границы")
                    table_name1.delete(0, END)
                    table_name1.focus_set()
                    break
                else:
                    count += 1
            if step.isalpha() == True or step_set.issubset(n) == False or float(step) < 0:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для шага")
                table_name2.delete(0, END)
                table_name2.focus_set()
            else:
                count += 1
            if eps.isalpha() == True or eps_set.issubset(n) == False:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для точности")
                table_name3.delete(0, END)
                table_name3.focus_set()
            else:
                count += 1
            if number_of_iterations.isalpha() == True or number_of_iterations_set.issubset(n) == False or float(
                    number_of_iterations) < 0:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы для итераций")
                table_name4.delete(0, END)
                table_name4.focus_set()
            else:
                count += 1
            if count == 5:
##                table_name1.config(state="readonly")
##                table_name2.config(state="readonly")
##                table_name3.config(state="readonly")
##                table_name4.config(state="readonly")
                graph(float(edges[0]), float(edges[1]), float(eps),float(step))

        else:
            messagebox.showerror("Ошибка!", "Введено недостаточное количество вхлдных параметров")
            '''table_name1.delete(0, END)
            table_name2.delete(0, END)
            table_name3.delete(0, END)
            table_name4.delete(0, END)
            table_name1.focus_set()'''

    if key == "Справка":
        messagebox.showinfo("Справка",
                            "Это приложение разработано для нахождения корней заданной функции.\n"
                            "\nСоздал это приложение Турсунов Жасурбек, студент группы ИУ7-26Б")

    if key == "Очистить поле ввода границ графика":
        table_name1.delete(0, END)
    if key == "Очистить поле ввода шага":
        table_name2.delete(0, END)
    if key == "Очистить поле ввода точности":
        table_name3.delete(0, END)
    if key == "Очистить поле ввода количества итераций":
        table_name4.delete(0, END)
    if key == "Очистить все поля":
        table_name1.delete(0, END)
        table_name2.delete(0, END)
        table_name3.delete(0, END)
        table_name4.delete(0, END)
        table_name1.focus_set()





#Лямбда функции
# Для очистки
clean1 = lambda x = "Очистить поле ввода границ графика": check(x)
clean2 = lambda x = "Очистить поле ввода шага": check(x)
clean3 = lambda x = "Очистить поле ввода точности": check(x)
clean4 = lambda x = "Очистить поле ввода количества итераций": check(x)
clean5 = lambda x = "Очистить все поля": check(x)

#для вычисления
find = lambda x = "Найти корни": check(x)
show_graph = lambda x = "Построить график": check(x)

#для справки
info = lambda x = "Справка": check(x)



#Верхнее меню
mainmenu = Menu(root)
root.config(menu = mainmenu)

usermenu = Menu(mainmenu, tearoff = 0)
usermenu.add_command(label = "Найти корни", command = find)
usermenu.add_command(label = "Построить график", command = show_graph)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Очистить поле ввода границ графика", command = clean1)
filemenu.add_command(label = "Очистить поле ввода шага", command = clean2)
filemenu.add_command(label = "Очистить поле ввода точности", command = clean3)
filemenu.add_command(label = "Очистить поле ввода количества итераций", command = clean4)
filemenu.add_command(label = "Очистить все поля", command = clean5)

mainmenu.add_cascade(label = "Действия", menu = usermenu)
mainmenu.add_cascade(label = "Очистить", menu = filemenu)
mainmenu.add_command(label = "Справка", command = info)


#Кнопка найти корни
button1 = Button(text = "Найти корни", width = 20, height = 2, font = "consolas 10 bold",bg="white",fg="#000080", command = find)
button1.grid(row = 3, column = 1)

#Кнопка Построить график
button2 = Button(text = "Построить график", width = 20, height = 2, font = "consolas 10 bold",bg="white",fg="#000080", command = show_graph)
button2.grid(row = 5, column = 1)

root.mainloop()
