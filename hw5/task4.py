def compute_digits_sum(num):
    sum = 0
    if num == 0: 
        return sum
    sum = (abs(num) % 10) + compute_digits_sum(abs(num) // 10)
    return sum

