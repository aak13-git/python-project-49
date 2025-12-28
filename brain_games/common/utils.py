import random


def get_name():
    name = input('May I have your name? ')
    return name


def greet(name):
    print(f'Hello, {name}!')


def welcome():
    print("Welcome to the Brain Games!")


def num_even():
    num = random.randint(1, 100)
    return num


def quest_even(num)->str:
    print(f'Question: {num}')

def exp_calc():
    num_1, num_2 = random.randint(1, 20), random.randint(1, 20)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    exp = f'{num_1} {random_operator} {num_2}'
    return exp


def quest_calc(exp):
    print(f'Question: {exp}')


def calculation(exp):
    num_1, operator, num_2 = exp.split(' ')
    match operator:
        case '+': return int(num_1) + int(num_2)
        case '-': return int(num_1) - int(num_2)
        case '*': return int(num_1) * int(num_2)


def result(answer: int, name: str, exp: int):
    if answer == calculation(exp):
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{calculation(exp)}'\n"
            f"Let's try again, {name}!"
        )


def random_num():
    num_1, num_2 = random.randint(1, 100), random.randint(1, 100)
    numbers = f'{num_1} {num_2}'
    return numbers

def quest_gcd(numbers):
    print(f'Question: {numbers}')

def calc_gcd(numbers):
    num_1, num_2 = numbers.split(' ')
    num_1, num_2 = int(num_1), int(num_2)
    if num_1 > num_2:
        alg = num_1 % num_2
        while num_2 % alg != 0:
            alg = num_2 % alg
        return alg
    elif num_1 < num_2:
        alg = num_2 % num_1
        while num_1 % alg != 0:
            alg = num_1 % alg
        return alg


def comparison(answer: int, numbers: int, name: str):
    if answer == calc_gcd(numbers):
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{calc_gcd(numbers)}'\n"
            f"Let's try again, {name}!"
        )






