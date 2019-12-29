from tkinter import *
from tkinter import messagebox
import random
import time as t

#Оформление окна
root = Tk()
root.title("Sorting")
root.geometry("820x500+250+100")
root.resizable(False, False)
root.iconbitmap("sorting.ico")


#Заголовок

head = Label(text = "Сортировка массива", font = "Helvetica 20 bold")
head.grid(row = 0, column = 0, columnspan = 4, pady = 10)

#поле ввода для первого массива
a1 = Label(text = "Введите размерность и диапазон для первого массива",font = "consolas 8 ")
a1.grid(row = 1, column = 0,columnspan = 12, pady = 10, padx = 10)
table_name1 = Entry(root, width = 50)
table_name1.grid(row = 2, padx = 10, column = 0, columnspan = 12, pady = 10, sticky = W)
table_name1.focus_set()
#поле ввода для второго массива
a2 = Label(text = "Введите размерность и диапазон для второго массива",font = "consolas 8 ")
a2.grid(row = 3, column = 0,columnspan = 12, pady = 10, padx = 10)
table_name2 = Entry(root, width = 50)
table_name2.grid(row = 4, padx = 10, column = 0, columnspan = 12, pady = 10, sticky = W)

# поле ввода для третьего массива
a3 = Label(text = "Введите размерность и диапазон для третьего массива",font = "consolas 8 ")
a3.grid(row = 5, column = 0,columnspan = 12, pady = 10, padx = 10)
table_name3 = Entry(root, width = 50)
table_name3.grid(row = 6, padx = 10, column = 0, columnspan = 12, pady = 10, sticky = W)

#Функция для выхода из окна вывода таблицы
def exit_run(window):
    window.destroy()
    table_name1.config(state = NORMAL)
    table_name2.config(state = NORMAL)
    table_name3.config(state = NORMAL)

# Функция для сортировки. Метод сортировки: Шелл
def test1(a):
    massiv = a.copy()
    t = len(massiv)//2
    while t > 0:
        for i in range(len(massiv) - t):
            j = i
            while j >= 0 and massiv[j] > massiv[j+t]:
                massiv[j], massiv[j+t] = massiv[j+t], massiv[j]
                j -= 1
        t = t // 2
    return massiv

# Замеры времени сортирвок массива
def zamer_time(mas):
    mas1 = []
    for i in mas:
        mas1.append(i)
    # Время выполнения сортировки Шеллом случайного массива:
    start = t.time()
    newmas = test1(mas)
    vr_slych = t.time()-start
    # Время выполнения сортировки Шеллом отсортированного массива:
    start = t.time()
    newmas = test1(newmas)
    vr_otsort = t.time()-start
    # Время выполнения сортировки Шеллом
    #обратно отсортированного массива:
    start = t.time()
    newmas.reverse()
    newmas = test1(newmas)
    vr_obratno_otsort = t.time()-start
    #print(mas1)
    # Время выполнения сортировки методом sort() случайного массива:
    start = t.time()
    newmas = mas1.sort()
    vr_sort = t.time()-start
    return vr_otsort,vr_slych,vr_obratno_otsort,vr_sort



def check(key):
    if key == "Вычислить" or key == "Вычислить время сортировки":
        m1 = (table_name1.get()).split()
        m2 = (table_name2.get()).split()
        m3 = (table_name3.get()).split()
        if len(m1) == 3 and len(m2) == 3 and len(m3) == 3:
            for i in range(3):
                n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"}
                a = set(m1[i])
                b = set(m2[i])
                c = set(m3[i])
                if m1[i].isalpha() == True or m2[i].isalpha() == True or m3[i].isalpha() == True or a.issubset(n) == False or b.issubset(n) == False or c.issubset(n) == False:
                    messagebox.showerror("Ошибка!", "Введены недопустимые символы")
                    table_name1.delete(0, END)
                    table_name2.delete(0, END)
                    table_name3.delete(0, END)
                    table_name1.focus_set()
                    break
                if m1[0].isdigit() == False or m2[0].isdigit() == False or m3[0].isdigit() == False:
                    messagebox.showerror("Ошибка!", "Введены недопустимые параметры")
                    table_name1.delete(0, END)
                    table_name2.delete(0, END)
                    table_name3.delete(0, END)
                    table_name1.focus_set()
                    break
                if (m1[1] > m1[2]) or (m2[1] > m2[2]) or (m3[1] > m3[2]):
                    messagebox.showerror("Ошибка!", "Введены недопустимые параметры")
                    table_name1.delete(0, END)
                    table_name2.delete(0, END)
                    table_name3.delete(0, END)
                    table_name1.focus_set()
                    break
            else:
                window = Toplevel(root)
                window.iconbitmap("sorting.ico")
                window.geometry("550x350+425+250")
                window.title("Таблица результатов")
                window.resizable(False, False)
                #########################################################################################
                b1 = Label(window, text="Вид", font="consolas 18 bold")
                b1.grid(row = 1, column = 1, columnspan = 4, pady = 10, padx = 10, sticky = W)

                c1 = Label(window, text="N1", font="consolas 18 bold")
                c1.grid(row = 1, column = 5, columnspan = 3, pady = 10, padx = 10)

                c2 = Label(window, text="N2", font="consolas 18 bold")
                c2.grid(row = 1, column = 12, columnspan = 3, pady = 10, padx = 10)

                c3 = Label(window, text="N3", font="consolas 18 bold")
                c3.grid(row = 1, column = 19, columnspan = 3, pady = 10, padx = 10)

                ##########################################################################################
                b2 = Label(window, text="Упорядоченный", font="consolas 15")
                b2.grid(row = 2, column = 1, columnspan = 4, pady = 10, padx = 10)

                b2_1 = Entry(window, width=15)
                b2_1.grid(row=2, column=5, columnspan=4, pady=10, padx=10)

                b2_2 = Entry(window, width=15)
                b2_2.grid(row=2, column=12, columnspan=4, pady=10, padx=10)

                b2_3 = Entry(window, width=15)
                b2_3.grid(row=2, column=19, columnspan=4, pady=10, padx=10)

                ##########################################################################################
                b3 = Label(window, text="Случайный", font="consolas 15")
                b3.grid(row = 3, column = 1, columnspan = 4, pady = 10, padx = 10, sticky = W)

                b3_1 = Entry(window, width=15)
                b3_1.grid(row=3, column=5, columnspan=4, pady=10, padx=10)

                b3_2 = Entry(window, width=15)
                b3_2.grid(row=3, column=12, columnspan=4, pady=10, padx=10)

                b3_3 = Entry(window, width=15)
                b3_3.grid(row=3, column=19, columnspan=4, pady=10, padx=10)

                ##########################################################################################
                b4 = Label(window, text="Обратный", font="consolas 15")
                b4.grid(row = 4, column = 1, columnspan = 4, pady = 10, padx = 10, sticky = W)

                b4_1 = Entry(window, width=15)
                b4_1.grid(row=4, column=5, columnspan=4, pady=10, padx=10)

                b4_2 = Entry(window, width=15)
                b4_2.grid(row=4, column=12, columnspan=4, pady=10, padx=10)

                b4_3 = Entry(window, width=15)
                b4_3.grid(row=4, column=19, columnspan=4, pady=10, padx=10)

                ##########################################################################################
                b5 = Label(window, text="Метод Sort", font="consolas 15")
                b5.grid(row = 5, column = 1, columnspan = 4, pady = 10, padx = 10, sticky = W)

                b5_1 = Entry(window, width=15)
                b5_1.grid(row=5, column=5, columnspan=4, pady=10, padx=10)

                b5_2 = Entry(window, width=15)
                b5_2.grid(row=5, column=12, columnspan=4, pady=10, padx=10)

                b5_3 = Entry(window, width=15)
                b5_3.grid(row=5, column=19, columnspan=4, pady=10, padx=10)

                ##########################################################################################

                back_button = Button(window, text="Закрыть", width=15, height=2,
                                     font="consolas 10 bold", bg="white", fg="#000080",
                                     command = lambda: exit_run(window))
                back_button.grid(row=6, padx=5, pady=10, column=19)
                ##########################################################################################

                #Вычисление времени для случайного вида
                massiv1 = [random.randint(int(m1[1]), int(m1[2])) for i in range(int(m1[0]))]
                massiv2 = [random.randint(int(m2[1]), int(m2[2])) for i in range(int(m2[0]))]
                massiv3 = [random.randint(int(m3[1]), int(m3[2])) for i in range(int(m3[0]))]

                tt1, tt2, tt3, tt4 = zamer_time(massiv1)
                tt5, tt6, tt7, tt8 = zamer_time(massiv2)
                tt9, tt10, tt11, tt12 = zamer_time(massiv3)

                b2_1.insert(END, "{:.3e} c".format(tt1))
                b2_2.insert(END, "{:.3e} c".format(tt5))
                b2_3.insert(END, "{:.3e} c".format(tt9))

                b3_1.insert(END, "{:.3e} c".format(tt2))
                b3_2.insert(END, "{:.3e} c".format(tt6))
                b3_3.insert(END, "{:.3e} c".format(tt10))

                b4_1.insert(END, "{:.3e} c".format(tt3))
                b4_2.insert(END, "{:.3e} c".format(tt7))
                b4_3.insert(END, "{:.3e} c".format(tt11))

                b5_1.insert(END, "{:.3e} c".format(tt4))
                b5_2.insert(END, "{:.3e} c".format(tt8))
                b5_3.insert(END, "{:.3e} c".format(tt12))

                field_list = [b2_1, b2_2, b2_3, b3_1, b3_2, b3_3, b4_1, b4_2, b4_3, b5_1, b5_2, b5_3]

                for x in field_list:
                    x.config(state="readonly")
                table_name1.config(state = "readonly")
                table_name2.config(state = "readonly")
                table_name3.config(state = "readonly")
                
                
        else:
            messagebox.showerror("Ошибка!","Недостаточное количество переменных")
            table_name1.delete(0, END)
            table_name2.delete(0, END)
            table_name3.delete(0, END)
    if key == '9' or key == '8' or key == '7' or key == '6' or key == '5' or key == '4' or key == '3' or key == '2' or key == '1' or key == '0':
        (root.focus_get()).insert(END, int(key))

    if key == '-':
        (root.focus_get()).insert(END, key)
    if key == "Справка":
        messagebox.showinfo("Справка",
                            "Это приложение разработано для вычисления времени сортировки массива.\n"
                            "\nСоздал это приложение Турсунов Жасурбек, студент группы ИУ7-26Б")

    if key == "Очистить поле ввода первого массива":
        table_name1.delete(0,END)
    if key == "Очистить поле ввода второго массива":
        table_name2.delete(0,END)
    if key == "Очистить поле ввода третьего массива":
        table_name3.delete(0,END)
    if key == "Очистить поле ввода для сортировки":
        table_name4.delete(0,END)
    if key == "Очистить поле вывода для сортировки":
        table_name5.delete(0,END)
    if key == "Очистить все поля" or key == 'C':
        table_name1.delete(0,END)
        table_name2.delete(0, END)
        table_name3.delete(0, END)
        table_name4.delete(0, END)
        table_name5.delete(0, END)
        table_name1.focus_set()

    if key == "Отсортировать введенный массив" or key == "Отсортировать":
        m4 = (table_name4.get()).split()
        for i in range(len(m4)):
            n = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"}
            l = set(m4[i])
            if m4[i].isalpha() == True or l.issubset(n) == False:
                messagebox.showerror("Ошибка!", "Введены недопустимые символы")
                table_name4.delete(0, END)
                table_name5.delete(0, END)
                table_name4.focus_set()
                break
        else:
            table_name5.config(state = NORMAL)
            for i in range(len(m4)):
                m4[i] = int(m4[i])
            s = test1(m4)
            s1 = ''
            for i in s:
                s1 = s1 + str(i) + ' '
            table_name5.insert(END, s1)
            messagebox.showinfo("Справка","Введенный массив успешно отсортирован")
            table_name4.delete(0, END)
            table_name5.delete(0, END)
            
            

#Лямбда функции
# Для очистки
clean1 = lambda x = "Очистить поле ввода первого массива": check(x)
clean2 = lambda x = "Очистить поле ввода второго массива": check(x)
clean3 = lambda x = "Очистить поле ввода третьего массива": check(x)
clean4 = lambda x = "Очистить поле ввода для сортировки": check(x)
clean5 = lambda x = "Очистить поле вывода для сортировки": check(x)
clean6 = lambda x = "Очистить все поля": check(x)

#для вычисления
translate1 = lambda x = "Вычислить время сортировки": check(x)
translate2 = lambda x = "Отсортировать введенный массив": check(x)
cmdcheck = lambda x = "Вычислить": check(x)
cmdcheck1 = lambda x = "Отсортировать": check(x)

#для справки
info = lambda x = "Справка": check(x)

#Верхнее меню
mainmenu = Menu(root)
root.config(menu = mainmenu)

usermenu = Menu(mainmenu, tearoff = 0)
usermenu.add_command(label = "Вычислить время сортировки", command = translate1)
usermenu.add_command(label = "Отсортировать введенный массив", command = translate2)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Очистить поле ввода первого массива", command = clean1)
filemenu.add_command(label = "Очистить поле ввода второго массива", command = clean2)
filemenu.add_command(label = "Очистить поле ввода третьего массива", command = clean3)
filemenu.add_command(label = "Очистить поле ввода для сортировки", command = clean4)
filemenu.add_command(label = "Очистить поле вывода для сортировки", command = clean5)
filemenu.add_command(label = "Очистить все поля", command = clean6)

mainmenu.add_cascade(label = "Действия", menu = usermenu)
mainmenu.add_cascade(label = "Очистить", menu = filemenu)
mainmenu.add_command(label = "Справка", command = info)


#Кнопка вычислитm
button1 = Button(text = "Вычислить", width = 20, height = 2, font = "consolas 10 bold",bg="white",fg="#000080", command = cmdcheck)
button1.grid(row = 7, padx = 5 , pady = 30, column = 1)

#Перевод массива онлайн

bottom = Label(text = "Проверка работы метода сортировки", font = "Helvetica 15 ")
bottom.grid(row = 5, column = 14, columnspan = 9, pady = 10)

table_name4 = Entry(root, width = 50)
table_name4.grid(row = 6, column = 14, columnspan = 12, pady = 10, padx = 10)

button2 = Button(text = "Отсортировать", width = 20, height = 2, font = "consolas 10 bold",bg="white",fg="#000080", command = cmdcheck1)
button2.grid(row = 7 , column = 16, columnspan = 2, pady = 10, padx = 10, sticky = W)

table_name5 = Entry(root, width = 50)
table_name5.grid(row = 8, column = 14,columnspan = 12, padx = 10, pady = 10)
table_name5.config(state = "readonly")



#Клавиатура
button_list = [

                '7', '8', '9',
                '4', '5', '6',
                '1', '2', '3',
                '0', 'C',  '-'
                ]
r = 1
c = 15
for i in button_list:
    cmd = lambda x=i: check(x)
    butt = Button(root, text=i, width = 10,bg="white",fg="#000080", command = cmd)
    butt.grid(row = r, column = c, ipadx = 30, padx = 10,pady = 10)
    c += 1
    if c > 17:
        c = 15
        r += 1

root.mainloop()
