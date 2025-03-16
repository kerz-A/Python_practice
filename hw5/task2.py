def solve_quadratic_equation(a, b, c):
    d = b**2 - (4 * a * c)
    result = []
    roots = ()
    if d > 0:
        count = 2
        x1 = (-b + d**(0.5)) / (2 * a)
        x2 = (-b - d**(0.5)) / (2 * a)
        
        if x1 > x2:
            x1, x2 = x2 , x1
        roots = (x1,x2)
        result.append(count)
        result.append(roots)
        return print(tuple(result))
        
    elif d == 0:
        count = 1
        x1 = -b / (2 * a)
        roots = (x1,)
        result.append(count)
        result.append(roots)
        return print(tuple(result))
    
    else:
        count = 0
        result.append(count)
        result.append(roots)
        return print(tuple(result))

