a = ['а ооо ооо ооlоо. ыыыы ааая  юююя. ауууuууу уууiо иия  в яя ёуо. с р тт',
     'аааа оууоу смр. ннл оа',
     'кнгп юиию счмт яяую. ааа ооо юуое',
     'рпрфк оенус. о6о',
     'ааа яуу оииrио юююы .  ууе оои.',
     ]

max_count = 0
s_max = ''
for i in ' '.join(a).split('.'):
    i = i.strip()
    count = 0
    for k in i.split():
        if set(k).issubset(set('ёуеоюиаыя')):
            count +=1
    if max_count < count:
        max_count = count
        s_max = i

if max_count == 0:
    print('Нет строк, где есть слова состоящие только из гласных букв')
print(s_max, max_count)
