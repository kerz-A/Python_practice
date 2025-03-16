def is_power(num, d = 2):
    if (num == d) or (num == 1): return True
    
    elif (num % d == 0) and (num != d):
        num = num / d
        return is_power(num, d)

    else:
        return False


print(is_power(1024))