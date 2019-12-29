from tkinter import *
from math import *

count_circles = 0
circles = list()
count_points = 0
points = list()
canH = 300
canW = 400
min_x, min_y, max_x, max_y, coef = 0, 0, 0, 0, 0
 
def solve():
    if count_points <= 1:
        print("Через данное количество точек нельзя провести прямую!")

    chosen = [-1, -1]
    max_in = -1
    for i in range(0, count_points - 1):
        for j in range(i + 1, count_points):
            if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                continue
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]

            cur_in = 0
            for k in range(0, count_circles):
                xc = circles[k][0]
                yc = circles[k][1]
                
                if fabs(x2 - x1) < 1e-7:
                    r = fabs(x2 - xc)
                elif fabs(y2 - y1) < 1e-7:
                    r = fabs(y2 - yc)
                else:
                    y = (xc - x1) * (y2 - y1) / (x2 - x1) + y1
                    x = (yc - y1) * (x2 - x1) / (y2 - y1) + x1
                    r = sqrt((x - xc) * (x - xc) + (y - yc) * (y - yc)) / 2

                if r <= circles[k][2]:
                    cur_in += 1
               

            if cur_in > max_in:
                chosen = [i, j]
                max_in = cur_in
                
    if max(chosen) == -1:
        print("Нельзя провести прямую через данные точки!")
    else:
        print("Выбранные точки:")
        print(chosen[0] + 1)
        print(chosen[1] + 1)
        for i in range(2):
            x_t = 10 + (points[chosen[i]][0] - min_x) * coef
            y_t = canH - (10 + (points[chosen[i]][1] - min_y) * coef)
            c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'red')

        fromX1 = 10 + (points[chosen[0]][0] - min_x) * coef
        fromY1 = 10 + (points[chosen[0]][1] - min_y) * coef
        toX1 = 10 + (points[chosen[1]][0] - min_x) * coef
        toY1 = 10 + (points[chosen[1]][1] - min_y) * coef
        if toY1 != fromY1:
            fromX = (0 - fromY1) / (toY1 - fromY1) * (toX1 - fromX1) + fromX1
            toX = (canH - fromY1) / (toY1 - fromY1) * (toX1 - fromX1) + fromX1
            fromY = canH
            toY = 0
        else:
            fromX = 0
            toX = canW
            fromY = canH - fromY1
            toY = canH - fromY1
        
        c.create_line(fromX, fromY, toX, toY)

    


count_circles = int(input("Введите количество окружностей: "))
print("Введите данные об окружности (координаты центра, радиус) через пробел:")
for i in range(count_circles):
    circles.append(list(map(int, input().split())))
count_points = int(input("Введите количество точек: "))
print("Введите координаты точек через пробел:")
for i in range(count_points):
    points.append(list(map(int, input().split())))

window = Tk()
window.title("Геометрия")
window.config(bg = "#eeeeee")
window.geometry("400x400")

c = Canvas(window, width = canW, height = canH, bg = 'white')
btn = Button(window, bg = "#dd0000", text = "Решить!", command = solve)
min_x = points[0][0]
min_y = points[0][1]
max_x = points[0][0]
max_y = points[0][1]

for i in range(1, count_points):
    x_t = points[i][0]
    y_t = points[i][1]
    if x_t > max_x:
        max_x = x_t
    if x_t < min_x:
        min_x = x_t
    if y_t > max_y:
        max_y = y_t
    if y_t < min_y:
        min_y = y_t
for i in range(0, count_circles):
    x_t = circles[i][0]
    y_t = circles[i][1]
    r_t = circles[i][2]
    if x_t + r_t> max_x:
        max_x = x_t + r_t
    if x_t - r_t < min_x:
        min_x = x_t - r_t
    if y_t + r_t > max_y:
        max_y = y_t + r_t
    if y_t - r_t < min_y:
        min_y = y_t - r_t
        
if min_x == max_x:
    coef_x = -1
else:
    coef_x = (canW - 20) / (max_x - min_x)
if min_y == max_y:
    coef_y = -1
else:
    coef_y = (canH - 20) / (max_y - min_y)
        
if coef_x > 0 and coef_y > 0:
    coef = min(coef_x, coef_y)

for i in range(0, count_circles):
    x_t = 10 + (circles[i][0] - circles[i][2] - min_x) * coef
    y_t = canH - (10 + (circles[i][1] - circles[i][2] - min_y) * coef)
    x_t_2 = 10 + (circles[i][0] + circles[i][2] - min_x) * coef
    y_t_2 = canH - (10 + (circles[i][1] + circles[i][2] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t_2, y_t_2, width = 4, outline = 'green')

for i in range(0, count_points):
    x_t = 10 + (points[i][0] - min_x) * coef
    y_t = canH - (10 + (points[i][1] - min_y) * coef)
    c.create_oval(x_t, y_t, x_t, y_t, width = 4, outline = 'black')

c.place(x = 0, y = 50)
btn.place(x = 180, y = 20)
window.mainloop()
