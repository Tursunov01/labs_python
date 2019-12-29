from math import*
from tkinter import*

def f(x):    
    #return x*x - 4
    #return cos(x)
    return x - cos(x)

def proizv(x):
    #return  2*x
    #return -sin(x)
    return 1 + sin(x)



def fi_f(x):
    if (proizv(x) == 0):
        l = 1 / (proizv(x - 0.1))
    else:
        l = 1 / (proizv(x))
    
    return x - l*f(x)

def root_search_point(a, eps, n):
    i = 0
    xpr = a
    while (i < n):
        i += 1
        y = f(xpr)
        fi = fi_f(xpr)
        x = fi
        if abs(x - xpr) < eps:
            return x, i, 0
        xpr = x        
    return 10 * '-', i, 1

def root_search(a, b, eps, n):
    i1 = i2 = i3 = 0
    x, i1, code = root_search_point(a, eps, n)
    if code != 0 or x > b or x < a:
        x, i2, code = root_search_point(b, eps, n)
    if code != 0 or x > b or x < a:
        x, i3, code = root_search_point(a + b/2, eps, n)
    i = i1 + i2 + i3
    if code == 0 and (x > b or x < a):
        #return 10 * '-', i, 2
        x, i, code = chast(a, b, eps, n)
        
    return x, i, code

def chast(x2, x1, e, n):
    k=0
    t = x2
    y = x1
    while abs(x2 - x1) > e:
            x0 = x1
            x1 = x2
            x2 = x1 - ((x0 - x1) * f(x1)) / (f(x0) - f(x1))
            print('x2   ',x2)
            k += 1
            if k >= n:
                x2 = 10*'-'
                code = 1
                break
    if y >= x2 >= t:
        if int(x2) == 0:
            x2 = int(x2)
        else:
            x2 = round(x2, 5)
            code = 0
    return x2, k, code


def solution(a, b, eps, h, n):    
    values = 1
    answer = 1
    error = 1
    func_range = 1
    counter = 1
    
    c1 = a
    c2 = a
    k = 0
    while(c2 < b):
        found = True
        x_sol = 0
        y_sol = 0
        err_code = 0
        n_iter = 1
        
        c2 += h
        
        if c2 > b:
            c2 = b        
       
        if abs(f(c1)) <= 1e-20:
            x_sol = c1
            y_sol = f(c1)
        elif abs(f(c2)) <= 1e-20:
            if c2 == b:
                x_sol = c2
                y_sol = f(c2)
            else:
                found = False
        elif f(c1)*f(c2) < 0:   # проверка интервала на наличие корней

            x_sol, n_iter, err_code = root_search(c1,c2,eps,n)
            if (x_sol > c2) and (x_sol > start) and(x_sol < end):
                x_sol = -x_sol
            
            if ((x_sol < start) or (x_sol > end)):
                found = False

            if err_code == 0:
                y_sol = f(x_sol)
        else:
            found = False

        if found:
           
            counter=(n_iter)
            error=(err_code)
            func_range=(str("(" + str("{:.3f}".format(c1)) + " ; " + str("{:.3f}".format(c2)) + ")"))
            if err_code == 0:
                values=("{:.3f}".format(x_sol))
                answer=("{:1.2e} ".format(y_sol))
            else:
                values=(12 * '-')
                answer=(12 * '-')
        c1 = c2

        return values, answer, error, func_range, counter

def process(a, b, h, e, ite):
    values = []
    answer = []
    error = []
    func_range = []
    counter = []
    i = a
    s = -1
    while i <= b - h:
        t = i
        y = i + h
        k = 0
        x2 = i
        x1 = i + h
        while abs(x2 - x1) > e:
            x0 = x1
            x1 = x2
            x2 = x1 - ((x0 - x1) * f(x1)) / (f(x0) - f(x1))
            k += 1
            if k >= ite:
                break
        if y >= x2 >= t:
            if int(x2) == 0:
                x2 = int(x2)
            else:
                x2 = round(x2, 5)
            values.append(x2)
            g = f(x2)
            answer.append("{:2.2e} ".format(g))
            #
            error.append(0)
            if int(i) == 0:
                i = 0
            elif int(i) == 1:
                i = 1
            elif i < 0:
                i = int(i)
            func_range.append(str("(" + str(i) + " ; " + str(i + h) + ")"))
            counter.append(k)
            s += 1
        i += h
    return values, answer, error, func_range, counter


def main():
    global start
    global end

    a = float(input("Введите значение левой границы: "))
    b = float(input("Введите значение правой границы: "))
    step = float(input("Введите длину шага: "))
    eps = float(input("Введите значение eps: "))
    n = int(input(("Введите  максимальное количество итераций: ")))

    #a, b, step, n, eps = 1,5,4,100,0.0001
    start = a
    end = b

    global values
    global answer
    global error
    global func_range
    global counter
    
    
    values = []
    answer = []
    error = []
    func_range = []
    counter = []

    flag = 1
  
    if flag == 1:
        ff = 0
        a1,b1= a, b
        num = 0
        while a < b:
            if((f(a) == 0) and (num != 0)):
                num -= 1 
            else:
                if ((a + step) > b):
                    val, ans, err, fun, cou = solution(a, b, eps, step, n)

                else:
                    val, ans, err, fun, cou = solution(a, a + step, eps, step, n)
                values.append(val)
                answer.append(ans)
                error.append(err)
                func_range.append(fun)
                counter.append(cou)
                
            a += step
            num += 1
        if (ff == 1):
            return
        if values == []:
            print("Ошибка!", 'Нет корней на [' +\
                                 str(a1) + '; ' + str(b1) + ']')
            
        
        table(values, answer, error, func_range, counter, n)
               
def table(values, answer, error, func_range, counter, n):
        booo = True
        i = 0
        while i < (len(func_range)):
                if func_range[i] == 1 or func_range[i] == [] :
                    s=values.pop(i)
                    s=answer.pop(i)
                    s=error.pop(i)
                    s=counter.pop(i)
                    s =func_range.pop(i)
                    i -= 1
                i += 1
        print(values)
        if len(values)==0:
            root_table = Tk()
            root_table.geometry('190x140+710+200')
            root_table.title("")
            b = Label(root_table, text=" Корней нет! ", font = 'Times 14')
            b.place(x=40,y=60,width = 105)
            
            make_grafik(start,end)
            mainloop()
            booo = False
        if (booo== True):
            root_table = Tk()
            root_table.geometry('+710+200')
            root_table.title("Таблица")
            i=0

            i = 0
            height = len(error)+5 
            width = 6
            for i in range(height - 4):
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
                                b = Label(root_table, text=str(i))
                            elif j == 1:
                                b = Label(root_table, text=func_range[i - 1])
                            elif j == 2:
                                b = Label(root_table, text=values[i - 1])
                            elif j == 3:
                                b = Label(root_table, text=answer[i - 1])
                            elif j == 4:
                                b = Label(root_table, text=counter[i - 1])
                            elif j == 5:
                                b = Label(root_table, text=error[i - 1])
                    b.grid(row=i, column=j)
                    
            b1 = Label(root_table, text="Код ошибки:")
            b2 = Label(root_table, text=' "0" - корень успешно найден')
            b3 = Label(root_table, text=' "1" - за '+ str(n)+ ' итерации(й) корень не был найден')
            b4 = Label(root_table, text=' "2" - невозможно вычислить корень данным методом')

            b1.grid(row=len(error)+2 , column=0, columnspan = 3, sticky = W)
            b2.grid(row=len(error)+3 , column=0,columnspan = 3, sticky = W)
            b3.grid(row=len(error)+4 , column=0,columnspan = 3, sticky = W)
            b4.grid(row=len(error)+5 , column=0,columnspan = 3, sticky = W)

            mainloop()




main()
