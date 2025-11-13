#include <iostream>
#include <vector>
using namespace std;

int f(vector<vector<int>>& matrix) {
    int maxv = matrix[0][0];
    int count = 0;
    for (auto& row : matrix) {
        for (int element : row) {
            if (element > maxv) {
                maxv = element;
                count = 1;
            } else if (element == maxv) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    int result = f(matrix);
    cout << result << endl;

    return 0;
}