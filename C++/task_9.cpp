#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

/**
 * Samir Galiev, NKAbd-02-25, 29.10.25, 10:46
 * Task 2. Vol. 9: 
 *    Даны 3 точки на плоскоси. 
 *    Определить, какая из точек ближе к началу координат.
 */

// Структура для хранения точки
struct Point {
    double x;
    double y;
};

// Функция для нахождения ближайшей точки к началу координат
pair<Point, double> closest_point(const vector<Point>& points) {
    Point closest = points[0];
    double min_distance = numeric_limits<double>::infinity();
    
    for (const auto& point : points) {
        double distance = sqrt(point.x * point.x + point.y * point.y);
        
        if (distance < min_distance) {
            min_distance = distance;
            closest = point;
        }
    }
    
    return make_pair(closest, min_distance);
}

int main() {
    cout << "Данная программа вычисляет какая из трех точек находится ближе к началу координат.\n" << endl;
    
    vector<Point> points;
    cout << "Введите координаты 3 точек:" << endl;
    
    // Ввод точек
    for (int i = 0; i < 3; i++) {
        Point p;
        cout << "\nТочка " << (i + 1) << ":" << endl;
        cout << "  x = ";
        cin >> p.x;
        cout << "  y = ";
        cin >> p.y;
        points.push_back(p);
    }
    
    // Использование функции
    auto result = closest_point(points);
    Point closest = result.first;
    double distance = result.second;
    
    cout << "\nБлижайшая точка: (" << closest.x << ", " << closest.y 
         << "), расстояние: " << distance << endl;
    
    return 0;
}