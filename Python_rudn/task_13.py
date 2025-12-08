'''
Samir Galiev, NKAbd-02-25, 10:48
Vol. 13, Task 2: Для задач темы «Структуры данных» написать функцию сортировки одного из полей структуры.
Определить структуру с именем Aeroflot, содержащую следующие поля: 
название пункта назначения; номер рейса; тип самолета.
'''

from collections import namedtuple

Aeroflot = namedtuple('Aeroflot', ['destination', 'flight_number', 'airplane_type'])

def sort_flights_by_field(flights_list, sort_key):
    return sorted(flights_list, key=lambda flight: getattr(flight, sort_key))

flights = []
n = int(input("Введите количество рейсов: "))

for i in range(n):
    print(f"\nВведите данные для рейса {i + 1}:")
    destination = input("Пункт назначения: ")
    flight_number = input("Номер рейса: ")
    airplane_type = input("Тип самолёта: ")
    flights.append(Aeroflot(destination, flight_number, airplane_type))

print("\nВыберите поле для сортировки:")
print("1. Пункт назначения")
print("2. Номер рейса")
print("3. Тип самолёта")
choice = input("Ваш выбор (1, 2 или 3): ")

if choice == "1":
    sort_field = "destination"
elif choice == "2":
    sort_field = "flight_number"
elif choice == "3":
    sort_field = "airplane_type"
else:
    sort_field = "destination"

sorted_flights = sort_flights_by_field(flights, sort_field)

print(f"\nОтсортированный список рейсов:")
for flight in sorted_flights:
    print(f"Пункт назначения: {flight.destination}, Номер рейса: {flight.flight_number}, Тип самолёта: {flight.airplane_type}")