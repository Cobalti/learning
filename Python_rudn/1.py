import math
import matplotlib.pyplot as plt

# Параметры: x от 0 до 4π, разбиваем на 1000 точек
num_points = 1000
x_min = 0
x_max = 4 * math.pi
step = (x_max - x_min) / (num_points - 1)

# Генерируем списки значений x, y, z
x_values = []
y_values = []
z_values = []

for i in range(num_points):
    x = x_min + i * step
    x_values.append(x)
    
    # Вычисляем y = 2·sin(5x) - 0.75·sin(3x)
    y = 2 * math.sin(5 * x) - 0.75 * math.sin(3 * x)
    y_values.append(y)
    
    # Вычисляем z = 0.3·cos(2x)·sin(x)
    z = 0.3 * math.cos(2 * x) * math.sin(x)
    z_values.append(z)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='y = 2·sin(5x) - 0.75·sin(3x)', linewidth=2)
plt.plot(x_values, z_values, label='z = 0.3·cos(2x)·sin(x)', linewidth=2)
plt.xlabel('x')
plt.ylabel('Значение функции')
plt.title('Графики зависимостей y(x) и z(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()