'''
Samir Galiev, NKAbd-02-25, 10:38
Vol. 11. Task 2(upd: task 2, Vol. 8): 
Подсчитать, сколько раз встречается в заданной целочисленной матрице A(N,M) максимальное по величине число.
'''

def f(matrix):
    maxv = matrix[0][0]
    count = 0
    for row in matrix:
        for element in row:
            if element > maxv:
                maxv = element
                count = 1
            elif element == maxv:
                count += 1
    return count

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = f(matrix)
print(result)