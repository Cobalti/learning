'''
 Samir Galiev, NKAbd-02-25, 29.10.25, 10:46
 Task 2. Vol. 9: 
    Даны 3 точки на плоскоси. 
    Определить, какая из точек ближе к началу координат.
'''

print('Данная программа вычисляет какая из трех точек находится ближе к началу координат.\n')
import math

def closet_point(points):
    f = None
    md = float('inf')
    for point in points:
        x, y = point
        distance = math.sqrt(x**2 + y**2)  # Формула расстояния
        
        if distance < md:
            md = distance
            f = point
    
    return f, md

points = []
print("Введите координаты 3 точек:")

for i in range(1, 4): # Ввод точек
    print(f"\nТочка {i}:")
    x = float(input("  x = "))
    y = float(input("  y = "))
    points.append((x, y))
closest, distance = closet_point(points) # Использование функции
print(f"Ближайшая точка: {closest}, расстояние: {distance}")