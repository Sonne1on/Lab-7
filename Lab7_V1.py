import numpy as np
from time import perf_counter
from random import randint


# Создадим и перемножим списки

start_1 = perf_counter() # Запуск таймера 1
sp_1 = [randint(0, 1000000) for i in range(1000001)]
sp_2 = [randint(0, 1000000) for i in range(1000001)]
mlp = []

for i in range(0,len(sp_1)):
    mlp.append(sp_1[i]*sp_2[i])
print(mlp)

end_1 = perf_counter()#Стоп таймер 1
finish_1 = end_1 - start_1 # Время затраченное на перемножене списков


# Создадим и перемножим массивы с помощью Numpy

start_2 = perf_counter()# Запуск таймера 2

mlp_arr = []
array_1 = np.random.randint(0, 1000000, 1000000)
array_2 = np.random.randint(0, 1000000, 1000000)

mlp_arr = np.multiply(array_1, array_2)
#print(mlp_arr)

end_2 = perf_counter() #Стоп таймер 2
finish_2 = end_2 - start_2 # Время затраченное на перемножение массивов


print()
print('__________________________________________________________')
print('Время перемножение списков  -', finish_1)
print('Время перемножение массивов -', finish_2)
print('__________________________________________________________')
print('Производительность метода Numpy в', finish_1/finish_2, 'выше')
