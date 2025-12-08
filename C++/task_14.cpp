#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>

using namespace std;

class TV {
private:
    string brand;
    int diagonal;
    bool IS4k;
    double price;

public:
    // Конструктор по умолчанию + с параметрами
    TV(const string& brand = "Unknown", int diagonal = 0, bool IS4k = false, double price = 0.0)
        : brand(brand), diagonal(diagonal), IS4k(IS4k), price(price) {}

    // Конструктор копирования
    TV(const TV& other)
        : brand(other.brand), diagonal(other.diagonal), IS4k(other.IS4k), price(other.price) {}

    // Геттер и сеттер
    double beriPRICE() const { return price; }
    void zadaiPRICE(double new_price) { price = new_price; }

    // Вывод
    void display() const {
        cout << "Brand: " << brand
             << ", Diagonal: " << diagonal << "\""
             << ", 4K: " << (IS4k ? "Yes" : "Fuck off bitch >:P")
             << ", Price: $" << price << endl;
    }

    // Перегрузка 1: без consider_price
    bool kakoe_govno_ti_kupil(const TV& other) const {
        if (diagonal != other.diagonal)
            return diagonal > other.diagonal;
        return IS4k && !other.IS4k;
    }

    // Перегрузка 2: с consider_price
    bool kakoe_govno_ti_kupil(const TV& other, bool consider_price) const {
        if (diagonal != other.diagonal)
            return diagonal > other.diagonal;
        if (IS4k != other.IS4k)
            return IS4k;
        if (consider_price)
            return price < other.price;
        return false;
    }

    // Статический метод: создание из строки
    static TV say_gex(const string& data_str) {
        vector<string> parts;
        istringstream ss(data_str);
        string part;
        while (getline(ss, part, ';')) {
            parts.push_back(part);
        }
        if (parts.size() < 4) {
            return TV(); // при ошибке --> обычный объект
        }

        string brand = parts[0];
        int diagonal = stoi(parts[1]);

        string is4k_str = parts[2];
        for (char& c : is4k_str) c = tolower(c);
        bool IS4k = (is4k_str == "true");

        double price = stod(parts[3]);

        return TV(brand, diagonal, IS4k, price);
    }
};

int main() {
    TV tv1;
    TV tv2("Samsung", 55, true, 700.0);
    TV tv3(tv2);
    TV tv4 = TV::say_gex("LG;65;True;900.0");

    cout << "TV1 (default):" << endl;
    tv1.display();

    cout << "TV2 (custom):" << endl;
    tv2.display();

    cout << "TV3 (copy):" << endl;
    tv3.display();

    cout << "TV4 (from string):" << endl;
    tv4.display();

    tv1.zadaiPRICE(299.99);
    cout << "\nTV1 new price: $" << tv1.beriPRICE() << endl;

    cout << "\nIs TV2 better than TV1 (size/4K only)? "
         << (tv2.kakoe_govno_ti_kupil(tv1) ? "Yes" : "No") << endl;

    TV tv5("Sony", 55, true, 649.99); // ← исправлена точка с запятой
    cout << "TV5:" << endl;
    tv5.display();

    cout << "Is TV5 better than TV2 (considering price)? "
         << (tv5.kakoe_govno_ti_kupil(tv2, true) ? "Yes" : "No") << endl;

    return 0;
}