'''
Samir Galiev, NKAbd-02-25
Vol. 12 Task 2: 
Определить структуру с именем Aeroflot, 
содержащую следующие поля: название пункта назначения; номер рейса; тип самолета.
'''


from collections import namedtuple

# Определяем структуру Aeroflot
Aeroflot = namedtuple('Aeroflot', ['destination', 'flight_number', 'airplane_type'])

# Ввод данных пользователем
destination = input("Введите пункт назначения: ")
flight_number = input("Введите номер рейса: ")
airplane_type = input("Введите тип самолёта: ")

# Создаём объект рейса
flight = Aeroflot(destination=destination, flight_number=flight_number, airplane_type=airplane_type)

# Выводим информацию
print("\nИнформация о рейсе:")
print(f"Пункт назначения: {flight.destination}")
print(f"Номер рейса: {flight.flight_number}")
print(f"Тип самолёта: {flight.airplane_type}")