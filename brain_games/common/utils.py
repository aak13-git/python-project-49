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





