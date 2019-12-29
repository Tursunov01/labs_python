#Турсунов Жасурбек
#ИУ7-16Б
#Лаб 10
#*****************************************************************************
def Vivod():
    outfile = open(filename)
    for line in outfile:
          print(line)
    outfile.close()


def Noviifail(filename):
     outfile= open(filename,'w')
     outfile.write('Фамилия'+' '*5)
     outfile.write('Алгебра'+' '*3)
     outfile.write ('Литература'+' '*3)
     outfile.write ('Химия'+' '*3+'\n')
     
     while True:
       fam=str(input('Введите фамилию ученика: '))
       q=12-len(fam)
       w=' '*q
       outfile.write(fam + w)
       alg=str(input('Введите оценку по алгебре: '))
       while True:
         try:
          if (0<=int(alg)<=5):
              outfile.write('  '+alg+'           ')
              break
          else:
             alg=str(input('Введите повторно оценку по алгебре: '))
         except ValueError:
             alg=str(input('Введите повторно оценку по алгебре: '))
             
       litra=str(input('Введите оценку по литературе: ')) 
       while True:
        try:
          if (2<=int(litra)<=5):
              outfile.write(litra+'         ')
              break
          else:
             litra = str(input('Введите повторно оценку по литературе: '))
        except ValueError:
            litra = str(input('Введите повторно оценку по литературе: '))
            
       him = str(input('Введите оценку по химии: '))
       while True:
        try:
          if (2<=int(him)<=5):
              outfile.write(him+'     ')
              outfile.write(' '+'\n')
              break
          else:
             him=str(input('Введите повторно оценку по химии: '))
        except ValueError:
            litra = str(input('Введите повторно оценку по химии: '))
            
       stop = (input('Если хотите закончить запись данных в файл, нажмите "1": '))
       try:
        if stop == '1':
           outfile.close()
           print()
           print('Файл: ')
           print()
           Vivod()
           break
       except ValueError:
           continue 
     
t = 0     
while True:
 print()
 print (
    ' '*7,' Меню: '
    '\n1) Выбор файла'
    '\n2) Создание нового набора записей'
    '\n3) Добавление записи'
    '\n4) Вывод всех записей'
    '\n5) Поиск по одному полю'
    '\n6) Поиск по двум полям'
    '\n0) Выход'
      )
 print()
 choice = input('Ваш выбор: ')
 if choice == '0':
        print ('Выход.')
        break
 elif choice == '1':
     
        print('\nВыбор файла.')
        print()
        
        filename =str(input('Введите имя файла, с которым хотите работать: '))
        if filename == '305.txt':
            t=1
            infile = open(filename)
            filename = '305(1).txt'
            outfile = open(filename,'w')                      
            for d in infile:
                outfile.write(d)
            outfile.write('\n')
            print('Записи исходного файла: ')
            print()
            outfile.close()
            infile.close()
            filename='305(1).txt'
            
            Vivod()
        else:
         Noviifail(filename)
       
 elif choice == '2':
     print('\nСоздание нового набора записей. ')
     print()
     t=0 
     filename= str(input('Введите название файла: '))
     Noviifail(filename)
     

 elif choice == '3':
     print('\nДобавление записи.')
     print()

     outfile = open(filename,'a')
   
     while True:
       fam=str(input('Введите фамилию ученика: '))
       q=12-len(fam)
       w=' '*q
       outfile.write(fam + w)
      
       alg=str(input('Введите оценку по алгебре: '))
       while True:
        
         try:
          if (2<=int(alg)<=5):
             outfile.write('  '+alg+'           ')
             break
          else:
             alg=str(input('Введите повторно оценку по алгебре: '))
         except ValueError:
             alg=str(input('Введите повторно оценку по алгебре: '))
             
       litra=str(input('Введите оценку по литературе: ')) 
       while True:
        try:
          if (2<=int(litra)<=5):
              outfile.write(litra+'         ')
              break
          else:
             litra = str(input('Введите повторно оценку по литературе: '))
        except ValueError:
            litra = str(input('Введите повторно оценку по литературе: '))
            
       him = str(input('Введите оценку по химии: '))
       while True:
        try:
          if (2<=int(him)<=5):
              outfile.write(him+'     ')
              outfile.write(' '+'\n')
              break
          else:
             him=str(input('Введите повторно оценку по химии: '))
        except ValueError:
            him = str(input('Введите повторно оценку по литературе: '))
            
       stop = (input('Если хотите закончить запись данных в файл, нажмите "1": '))
       try:
        if stop == '1':
           outfile.close()
           print()
           break
       except ValueError:
           continue 
     outfile=open(filename)
     print('Измененный файл: ')
     print()
     Vivod()
     
     
 elif choice == '4':
     print('\nВывод всех записей.')
     print()
     Vivod()

 elif choice == '5':
     print('Записи исходного файла: ')
     print()
     Vivod()   
     data = []
     outfile = open(filename)
     for line in outfile:
           data.append(line.split())
     if t == 1:
        nomer = str(input('№ поля, по которому будет выполняться поиск: '))
        while True:
          if (1<=int(nomer)<=4):
              break
          else:
             nomer = str(input('Введите повторно № поля, по которому будет выполняться поиск: '))
        print()
        res = []
        outf = open('data4.txt','w')
        familia= str(input('Введите значение поля: '))
        for i in range(len(data)-1):
            nomer1 = ((data[i][int(nomer)-1]).find(familia,0,len(data[i][int(nomer)-1])))
            if nomer1!=-1:
                res.append(' '.join(data[i]))

     elif t == 0:
        nomer = str(input('№ поля, по которому будет выполняться поиск: '))
        while True:
          if (1<=int(nomer)<=4):
              break
          else:
             nomer = str(input('Введите повторно № поля, по которому будет выполняться поиск: '))
        print()
        res = []
        outf = open('data4.txt','w')
        familia= str(input('Введите значение поля: '))
        for i in range(len(data)-1):
            nomer1 = ((data[i][int(nomer)-1]).find(familia,0,len(data[i][int(nomer)-1])))
            if nomer1!=-1:
                res.append(' '.join(data[i]))
     if len(res) == 0:
         print("В исходном файле нет полей, удовлетворяющих Вашему запросу")
     else:
         print()
         for i in range(len(res)):
              print(res[i])
              outf.write(res[i] + '\n')
                     
 elif choice == '6':
     print('\nПоиск по двум полям.')
     print()
     print('Записи исходного файла: ')
     print()
     Vivod()   
     data = []
     outfile = open(filename)
     for line in outfile:
           data.append(line.split())
     if t == 1:
        nomer = str(input('№ поля, по которому будет выполняться поиск: '))
        
        while True:
          if (1<=int(nomer)<=4):
              break
          else:
             nomer = str(input('Введите повторно № поля, по которому будет выполняться поиск: '))
        nomerr = str(input('Cледующий № поля, по которому будет выполняться поиск: '))
        while True:
          if (1<=int(nomerr)<=4):
              break
          else:
             nomerr = str(input('Введите повторно Cледующий  № поля, по которому будет выполняться поиск: '))
        print()
        res = []
        outf = open('data4.txt','w')
        familia= str(input('Введите значение первого выбранного поля: '))
        familia1= str(input('Введите значение второго выбранного поля: '))
        for i in range(len(data)-1):
            nomer1 = ((data[i][int(nomer)-1]).find(familia,0,len(data[i][int(nomer)-1])))
            nomer111 = ((data[i][int(nomerr)-1]).find(familia1,0,len(data[i][int(nomer)-1])))
            if nomer1!=-1 and nomer111!=-1:
                res.append(' '.join(data[i]))


     elif t == 0:
        nomer = str(input('№ поля, по которому будет выполняться поиск: '))
        
        while True:
          if (1<=int(nomer)<=4):
              break
          else:
             nomer = str(input('Введите повторно № поля, по которому будет выполняться поиск: '))
        nomerr = str(input('Cледующий № поля, по которому будет выполняться поиск: '))
        while True:
          if (1<=int(nomerr)<=4):
              break
          else:
             nomerr = str(input('Введите повторно Cледующий  № поля, по которому будет выполняться поиск: '))
        print()
        res = []
        outf = open('data4.txt','w')
        familia= str(input('Введите значение первого выбранного поля: '))
        familia1= str(input('Введите значение второго выбранного поля: '))
        for i in range(len(data)-1):
            nomer1 = ((data[i][int(nomer)-1]).find(familia,0,len(data[i][int(nomer)-1])))
            nomer111 = ((data[i][int(nomerr)-1]).find(familia1,0,len(data[i][int(nomer)-1])))
            if nomer1!=-1 and nomer111!=-1:
                res.append(' '.join(data[i]))

     if len(res) == 0:
         print("В исходном файле нет полей, удовлетворяющих Вашему запросу")
     else:
         print()
         for i in range(len(res)):
              print(res[i])
              outf.write(res[i] + '\n')
     

