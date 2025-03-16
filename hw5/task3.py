def solve_quadratic_equation(a, b, c):
    d = b**2 - (4 * a * c)

    if d > 0:
        
        x1 = (-b + d**(0.5)) / (2 * a)
        x2 = (-b - d**(0.5)) / (2 * a)
        
        if x1 > x2:
            x1, x2 = x2 , x1

        return (2,(x1,x2))
        
    elif d == 0:
        x1 = -b / (2 * a)
        return (2,(x1,))
        
    
    else:
        return(0, ())

print(solve_quadratic_equation(2, -3, -20))