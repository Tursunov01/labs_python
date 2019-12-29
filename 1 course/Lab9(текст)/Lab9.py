#Турсунов Жасурбек
#ИУ7-16Б
#Лаб 9
#*****************************************************************************
MENU = [
        '  0. Exit',
        '  1. Выравнивание по ширине',
        '  2. Выравнивание по левому краю',
        '  3. Выравнивание по правому краю',
        '  4. Замена во всем тексте одного слова другим',
        '  5. Удаление заданного слова из текста',
        '  6. Замену ариф. выражений, состаящих из сложения и вычитанияб на результат их вычисление',
        '  7. В каждом четном предложении  наити наименее часто встречающийся символ\n     (из символов вообще присутствующих в предложении)'
        ]
#*****************************************************************************
#function get input from file
def inputt():
    fi = 'input.txt'
    f = open(fi)
    a = f.readlines()
    f.close()
    return a
#*****************************************************************************
#function to find max length of lines
def maxx():
    m = len(a[0])
    for i in a:
        if m<len(i): m = len(i)
    return m
#*****************************************************************************
def output():
    #os.system('cls')
    print('\n',MENU[k],'\n')
    
    for i in a:
        print(' '*10,i) 
    print('\n'+'*'*50) 
#*****************************************************************************
#'  1. Выравнивание по ширине'
def def1():
    for i in range(len(a)):
        n = len(list(a[i].split()))
        if n == 1: continue
        space = m - len(a[i]) 
        t = (space//(n-1)+1)
        a[i] = a[i].replace(' ',' '*t)
        a[i] = a[i].replace(' '*t,' '*(t+1),space % (n-1))
#*****************************************************************************
#'  2. Выравнивание по левому краю'
def def2():
    for i in range(len(a)):
        a[i] = a[i].lstrip()
#*****************************************************************************
#'  3. Выравнивание по правому краю'
def def3():
    for i in range(len(a)):
        a[i] = ' '*(m - len(a[i])) +a[i]
#*****************************************************************************
#'  4. Замена во всем тексте одного слова другим'
def def4(st1,st2):
    st1 = ' ' + st1 + ' '
    st2 = ' ' + st2 + ' '
    for i in range(len(a)):
        s = ' '+a[i]+' '
        while st1 in s:
            s = s.replace(st1,st2)
        a[i] = s[1:len(s)-1]
#*****************************************************************************
#'  5. Удаление заданного слова из текста'
def def5(st):
    st = ' ' + st + ' '
    for i in range(len(a)):
        s = ' ' + a[i] + ' '
        s = s.replace(st,' ')
        a[i] = s[1:len(s)-1]

#*****************************************************************************
#'  6. Замену ариф. выражений, состаящих из сложения и вычитанияб на результат их вычисление',
def def6():
    for i in range(len(a)):
        st = a[i].split()
        j = 1
        while j< len(st)-1:
            if st[j] in ['+','-']:
                try:
                    x = float(st[j-1])
                    y = float(st[j+1])
                    if st[j] == '+':
                        k = x+y
                        if (x+y)- int(x+y) ==0: k = int(k)
                    else:
                        k = x-y
                        if (x-y)- int(x-y) ==0: k = int(k)
                    st[j] = '{}'.format(k)
                    st.pop(j-1)
                    st.pop(j)
                    j -=1
                except:
                    pass 
            j += 1
        a[i] = ' '.join(st)
#*****************************************************************************
def check(st):
    minn = 0
    cim = ''
    try:
        s = st
        s.strip()
        n = len(st)
        minn = n
        cim = s[0]
        while s != '' :
            s.strip()
            count = s.count(s[0])
            if minn> count :
                minn = count
                cim = s[0]
            if minn == 1: break
            s = s.replace(s[0],'')
    except: pass
    return cim,minn
#*****************************************************************************
def output2():
    print('*'*50,'\n')
    for i in range(len(b)):
        print(' '*10,i+1,'   ',b[i], end = '.\n')
    print('\n'+'*'*50)     
#*****************************************************************************
def def7():
    global b
    b = (' '.join(a)+' ').split('. ')
    menu(before)
    for i in range(1,len(b),2) :
        result.append(check(b[i]))
#*****************************************************************************
def def8():
    maxx = check(b[0])
    t = 0
    st = b[0]
    for i in range(1,len(b)):
        k = check(b[i])
        if k > maxx:
            t = i
            maxx  = k
            st = b[i]
    print('*'*50)
    print('Result:')
    print('Предложение {} : {}'.format(t+1,st))
    print('Количество Слов {}'.format(maxx))
#*****************************************************************************
#Chuan Hoa Xau St
def Hola(st):
    st = st.strip()
    while '  ' in st:
        st = st.replace('  ',' ')
    return st    
#*****************************************************************************
def printMenu():
    #os.system('cls') 
    print('*'*50)
    print()
    print('Menu \n')
    for i in MENU:
        print(i)
    print()
    print('*'*50)
    while True:
        try:
            while True:
                i = int(input('Input Your Choose: '))
                if 0<=i<=7: return i
        except:
            pass 
#*****************************************************************************
def inputWord(st):
    while True:
        try:
            st = input(st).strip().split()[0]
            if st != '': return st
        except: 
            print('Input Again!!!')
#*****************************************************************************        
def menu(i):
    if i ==1: def1()
    if i ==2: def2()
    if i ==3: def3()
    if i ==4:
        st1 = inputWord('Input First Word :  ')
        st2 = inputWord('Input Second Word:  ')
        def4(st1,st2)
    if i ==5:
        st = input('Input Word To Delete:  ')
        def5(st)
    if i ==6: def6()
    if i ==7: 
        def7()
    global m
    m = maxx()
    if i in [4,5,6,7,8]:
        menu(before)
    


#*****************************************************************************
def output1():
    print(' '*10,'Result:')
    print(' '*10,'{:^10} {:^10} {:^10}'.format('Number','alphabet','times')) 
    for i in range(len(result)) :
        print(' '*10,'{:^10} {:^10} {:^10}'.format(2*i+2,result[i][0],result[i][1])) 
    #print('\n','*'*50,'\n')  
#*****************************************************************************

a = ['Что объединяет всех нас - живущих на земном шаре? Желание успеха, славы, почестей, высокого положения?',
     'Конечно, это может выглядеть привлекательным, но все это не сближает людей.',
     'По-настоящему объединить нас может только любовь.',
     'Почему  мы любим футбол? Что может дать нам обыкновенная пара ворот и самый обыкновенный мяч?',
     'Все дело в любви к этой игре, которая всегда отвечает взаимностью.',
     'Влюбленные в футбол, мы переживаем взлеты и падения, падаем на колени и каждый раз поднимаемся и встаем во весь рост.',
     '15 + 7 Мы бросаем вызов самим себе, сопернику, обстоятельствам и побеждаем. 14 - 8',
     ]
b = []
for i in range(len(a)):
    a[i] = Hola(a[i])
result = []
#s = list(a)
m = maxx()
before = 2
while True:
    try:
        k = printMenu()
        if k ==0:
            print('Finished ')
            break
        menu(k)
        output()
        if k == 7:
            output1()
            output2()
        #if not input('Press A NUMBER to return to Menu \nThe Rest to Exit\n').isdigit(): break 
        #a = list(s)
        for i in range(len(a)):
            a[i] = Hola(a[i])
        if k in [1,2,3]: before = k
        result = []
    except:
        print('Finished')
        break
