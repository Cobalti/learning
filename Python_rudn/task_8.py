'''
Samir Galiev, NKAbd-02-25 11:15
Task 2. Vol. 8: 
2.	Подсчитать, сколько раз встречается 
в заданной целочисленной матрице 
A(N,M) максимальное по величине число.
'''
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

maxv = matrix[0][0]
count = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maxv:
            maxv = matrix[i][j]
            count = 1
        elif matrix[i][j] == maxv:
            count += 1

print(count)
