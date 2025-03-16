""" манх - сумма модулей разностей их координат
эвкл - корень из суммы разностей квадратов их координат """

def compute_nearest_neighbour(p1, *points):   
    len = (lambda a, b : abs(a[0] - b[0]) + abs(a[1] - b[1]), p1, *points)
    manh = (map(len, p1, *points))
    return manh
    
print(list(compute_nearest_neighbour((0, 0), ((1, 5), (3, 4)))))