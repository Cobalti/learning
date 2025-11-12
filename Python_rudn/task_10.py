'''
Samir Galiev, NKAbd-02-25, 05.11.25, 10:50
Task 2. Vol. 10: В массиве из n чисел найти первый отрицательный элемент и его индекс в массиве.
(с использованием функции)
'''

print("Данная программа находит первый отрицательный элемент и его индекс в массиве с использованием функции.")

#создание массива 
def array():
    n = int(input("Введите количество элементов: "))
    arr = []
    for i in range(n):
        arr.append(float(input(f"Элемент {i+1}: ")))
    return arr

#поиск отрицательного элемента
def find(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            return arr[i], i
    return None, -1

# Основная программа
a = array()
print(f"Ваш массив: {a}")

number, index = find(a)

if number is not None:
    print(f"Первый отрицательный элемент: {number}")
    print(f"Индекс: {index}")
else:
    print("Отрицательных элементов нет") 
    