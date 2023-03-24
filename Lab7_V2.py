import numpy as np
import matplotlib.pyplot as plt

# Вопрос 2 вариант 1

arr = np.genfromtxt('data1.csv', delimiter=';')
arr = arr[0:]
data = np.array(arr[:, 0], float)
x = data[~np.isnan(data)]
data = np.array(arr[:, 4], float)
y1 = data[~np.isnan(data)]
data = np.array(arr[:, 5], float)
y2 = data[~np.isnan(data)]
y3 = (y1+y2)/2
fig, (ax1, ax2) = plt.subplots(figsize=(15, 8), ncols=2)
fig.suptitle("График", size=22)

ax1.plot(x,y1, label=fr"$Обороты двигателя$")
ax1.plot(x,y2, label=fr"$Обороты холостого хода$")
ax1.set_title("Изменение об. двигателя", size=18)
ax1.set_xlabel("Время, с", size=16)
ax1.set_ylabel("Кол-во об. двигателя", size=16)

ax2.plot(x,y3, label=fr"$Корреляция$")
ax2.set_title("График корреляции", size=18)
ax2.set_xlabel("Время, с", size=16)
ax2.set_ylabel("Кол-во об. двигателя", size=16)

plt.show()
