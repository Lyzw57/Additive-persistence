# def add_digits(number):
#     """
#     returns sum of digits. Version with strings.
#     """
#     digits = [int(digit) for digit in str(number)]
#     return sum(digits)

def add_digits(number):
    """
    returns sum of digits without converting into string.
    """
    sum_of_digits = 0
    while number:
        sum_of_digits += number % 10
        number //= 10

    return sum_of_digits

def add_persistence(number):
    persistence = 0
    while number > 9:
        number = add_digits(number)
        persistence += 1
   
    return persistence

if __name__ == '__main__':
    for example in (13, 1234, 9876, 199):
        print(example, add_persistence(example))