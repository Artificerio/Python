from scipy import random 
import numpy as np
import matplotlib as pl

#Пределы интегрирования
a = 0
b = 42
#Количетсво реализация
N = 100
xrand = np.zeros(N)
#Каждому элементу присвоить случайно значение
for i in range (len(xrand)):
    xrand[i] = random.uniform(a,b)

#Определим нашу функцию
def func(x):
    return 1 + (x-22)*(x-22)
integral = 0.0

#Присваиваем случайное значение функции
for i in range(N):
    integral+=func(xrand[i])

#По формуле находим приближенное значение
answer = (b-a)/float(N) * integral
print(answer)





