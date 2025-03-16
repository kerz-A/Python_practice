def int_filter(numbers):
    return filter(lambda x: x.is_integer(), numbers)

def digits_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

input_string = "0.5 2 2 5 11 10.5 12 -21 1 -8 9 0"

input_numbers = map(float, input_string.split())

int_numbers = list(map(int,(int_filter(input_numbers))))

sort1 = sorted(int_numbers, key = lambda x: (x <= 0, abs(x)))

sort2 = sorted(int_numbers, key = lambda x: (digits_sum(x), x))

sort3 = sorted(int_numbers, key = lambda x: (x % 2 == 1, -x if x % 2 == 1 else x))

print(sort1, sort2, sort3)