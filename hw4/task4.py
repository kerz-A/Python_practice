print('Входные данные:')

matrix_range = ([int(x) for x in input().split(' ')])


matrix = []
matrix_row = []
matrix_cols = []


for col in range(matrix_range[0]):
    matrix_row = ([int(x) for x in input().split(' ')])
    matrix.append(matrix_row)

print('Вывод программы:')

if matrix_range[0] == matrix_range[1]:
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            print(j)
            if matrix[i][j] == 0:
                print('Матрица верхнетреугольная')


""" if matrix_range[0] == matrix_range[1]:
    for row in matrix:
        for j in range(len(row)):
            if (row[j - 1] == 0)
                print('Матрица диагональная')  """               


if matrix_range[0] == matrix_range[1]:
    for row in range(len(matrix)):
        #print(row)
        if matrix[row][row] == 1:
            print('Матрица Матрица единичная')



print(matrix)






        
        
