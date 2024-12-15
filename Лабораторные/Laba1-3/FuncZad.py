
def greet(name):
    print(f'Здравствуйте, {name}!')

greet('Леха')



def square(num):
    return num**2

print(square(9))

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(max_of_two(6, 2))

def describe_person(name, age=30):
    print(name, '-', age, 'лет')

describe_person('Леха')
describe_person('Рома', 26)

def is_prime(number):
    if number != 1:
        flag = True
        for i in range(2, number // 2):
            if number % i == 0:
                flag = False
    else:
        flag = False
    return flag

for i in range(1, 101):
    print(i, is_prime(i))


