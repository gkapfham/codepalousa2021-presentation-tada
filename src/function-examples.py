from typing import List

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


def is_subset(one: List, two: List) -> bool:
    for element_one in one:
        matched = False
        for element_two in two:
            if element_one == element_two:
                matched = True
                break
        if not matched:
            return False
    return True


sum_digits = add_digits("123")
print(sum_digits)

factorial_value = factorial(3)
print(factorial_value)

list_one = [1,2,3,4]
list_two = [1,2,3,4,5]
found_subset = is_subset(list_one, list_two)
print(found_subset)
