/*
Samir Galiev, NKAbd-02-25
Vol. 12 Task 2: 
Определить структуру с именем Aeroflot, 
содержащую следующие поля: название пункта назначения; номер рейса; тип самолета.
*/
#include <iostream>
#include <string>


using namespace std;
// Определяем структуру Aeroflot
struct Aeroflot {
    string destination;
    string flight_number;
    string airplane_type;
};


int main() {
    string destination, flight_number, airplane_type;

    // Ввод данных пользователем
    cout << "Введите пункт назначения: ";
    getline(cin, destination);

    cout << "Введите номер рейса: ";
    getline(cin, flight_number);

    cout << "Введите тип самолёта: ";
    getline(cin, airplane_type);

    // Создаём объект рейса
    Aeroflot flight{destination, flight_number, airplane_type};

    // Выводим информацию
    cout << "\nИнформация о рейсе:\n";
    cout << "Пункт назначения: " << flight.destination << "\n";
    cout << "Номер рейса: " << flight.flight_number << "\n";
    cout << "Тип самолёта: " << flight.airplane_type << "\n";

    return 0;
}