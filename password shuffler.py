import random
a = '123456789'
b = 'qwertyuiopasdfgh'
c = b.upper()
#соединяем все строки
d = a+b+c
#преобразуем в список
ls = list(d)
#мешаем
random.shuffle(ls)
#извлекаем 12 произвольных значений
totl = ''.join([random.choice(ls) for x in range(12)])
print(totl)
input("Нажми ENTER чтобы выйти")

