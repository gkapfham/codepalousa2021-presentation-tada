def add_digits(digits: str) -> int:
    value = 0
    for digit in digits:
        value += int(digit)
    return value

def factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


sum_digits = add_digits("123")
print(sum_digits)

factorial_value = factorial(3)
print(factorial_value)
