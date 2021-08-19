def add_digits(digits: str) -> int:
    value = 0
    for digit in digits:
        value += int(digit)
    return value


sum_digits = add_digits("123")
print(sum_digits)
