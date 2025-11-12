/*
NKAbd-02-25, Samir Galiev, 09.11.25
Vol. 10, Task 2: 
В массиве из n чисел найти первый отрицательный элемент и его индекс в массиве.
(с использованием функции)
*/
#include <iostream>
#include <vector>
using namespace std;

// Получить массив
vector<double> getArr(int n) {
    vector<double> arr(n);
    for (int i = 0; i < n; i++) {
        cout << "Число " << i << ": ";
        cin >> arr[i];
    }
    return arr;
}

// Найти отрицательный
void findNeg(vector<double> arr) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] < 0) {
            cout << "Найден: " << arr[i] << " на позиции " << i << endl;
            return;
        }
    }
    cout << "Отрицательных нет" << endl;
}


int main() {
    int n;
    cout << "Размер массива: ";
    cin >> n;
    
    vector<double> arr = getArr(n);
    findNeg(arr);
    
    return 0;
}