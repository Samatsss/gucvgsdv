
#ДЕЛАЕМ СРЕЗЫ(1)

#st = 'Pomidor'
#print(st[2])
#print(st[-2])
#print(st[0:5])
#print(st[0:5])
#print(st[0] + st[2] + st[4] + st[6])
#print(st[1] + st[3] + st[5])
#print(st[::-1])
#print(st[::-2])
#print(len(st))





#КОЛИЧЕСТВО СЛОВ(2)

#x = 'I really love tomatoes'
#print(x.count(" ") + 1)





#ДВЕ ПОЛОВИНКИ(3)

#strn = 'Sigara'
#print(strn[3:6] + strn[0:3])





#ПЕРВОЕ И ПОСЛЕДНЕЕ ВХОЖДЕНИЕ(4)

#x = 'fSamatf'
#print(x.count('f'))




#УДАЛЕНИЕ ФРАГМЕНТА(5)

#string = 'hSamathdddddd'
#x = (string.find('h'))
#y = (string.rfind('h'))
#print(string[:x] + string[y:])





#ЗАМЕНА ПОДСТРОКИ(6)
#st = 162512
#print(str(st).replace(str(1),'one'))




#УДАЛЕНИЕ СИМВОЛА(7)

#st = 'hbcbhue@@mail.ru'
#print(st.replace('@',''))




#ЗАМЕНА ВНУТРИ ФРАГМЕНТА(8)

#st = 'httpsh://Samath.com'
#h1 = st.find('h')
#h2 = st.rfind('h')
#x = st[h1 + 1:h2]
#z = x.replace('h', 'H')
#print(z)




#МИНИМУМ ИЗ ДВУХ ЧИСЕЛ(9)

#a = int(input())
#b = int(input())
#if a>b:
#    print(b)
#else:
#    print(a)




#ЗНАК ЧИСЛА(10)

#x = float(input("Введите число x: "))
#if x > 0:
#    sign_x = 1
#elif x < 0:
#    sign_x = -1
#else:
#    sign_x = 0
#print("Значение sign(x):", sign_x)





#ШАХМАТНАЯ ДОСКА(11)

#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if 1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8:
#    if (x1+y1)%2 == (x2+y2)%2:
#        print('YES')
#    else:
#        print('NO')
#else:
#    print('Такой клеточки нет')



#ВИСОКОСНЫЙ ГОД(12)

#year = int(input("Введите год: "))
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("YES")
#else:
#    print("NO")



#ШОКОЛАДКА(13)

#n = int(input("Введите n: "))
#m = int(input("Введите m: "))
#k = int(input("Введите k: "))
#if (k <= n * m) and ((k % n == 0) or (k % m == 0)):
#    print("YES")
#else:
#    print("NO")




#ЯША ПЛАВАЕТ В БАССЕЙНЕ(14)

#a = int(input("Введите a: "))
#b = int(input("Введите b: "))
#x = int(input("Введите x: "))
#y = int(input("Введите y: "))
#dst = min(x, y, a-x, b-y)
#print("Минимальное расстояние до бортика: ", dst)



