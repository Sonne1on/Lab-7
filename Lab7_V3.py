import matplotlib.pyplot as plt
import numpy as np

# Вопрос 3

сx = np.linspace(-np.pi, np.pi, 50)              # задаем функции для графика
сy = сx
сz = np.tan(сx)

fig = plt.figure()                                  # строим график
ax = fig.add_subplot(111, projection='3d')
ax.plot(сx, сy, сz, label = '3D график')
plt.show()
