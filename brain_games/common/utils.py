import random
from math import sqrt

NUM_MIN = 1
NUM_MAX = 100
RANDOM_NUM_1 = random.randint(NUM_MIN, NUM_MAX)  # NOSONAR
RANDOM_NUM_2 = random.randint(NUM_MIN, NUM_MAX)  # NOSONAR
STEP_MIN_NUM = 1
STEP_MAX_NUM = 10
LENGTH_MIN = 5
LENGTH_MAX = 10
NUM_PRIME_MIN = 2
NUM_PRIME_MAX = 3571
CORRECT_ANSWER = 'Correct!'
PASS = '..'


def get_name():
    name = input('May I have your name? ')
    return name


def greet(name):
    print(f'Hello, {name}!')


def welcome():
    print("Welcome to the Brain Games!")


def num_even():
    num = random.randint(NUM_MIN, NUM_MAX)  # NOSONAR

    return num


def quest_even(num) -> str:

    print(f'Question: {num}')


def exp_calc():

    num_1, num_2 = (
        random.randint(NUM_MIN, NUM_MAX),  # NOSONAR
        random.randint(NUM_MIN, NUM_MAX)  # NOSONAR
    )
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)  # NOSONAR
    exp = f'{num_1} {random_operator} {num_2}'
    return exp


def quest_calc(exp):

    print(f'Question: {exp}')


def calculation(exp):
    num_1, operator, num_2 = exp.split(' ')
    match operator:
        case '+':
            return int(num_1) + int(num_2)
        case '-':
            return int(num_1) - int(num_2)
        case '*':
            return int(num_1) * int(num_2)


def result(answer: int, name: str, exp: int):
    if answer == calculation(exp):
        print(CORRECT_ANSWER)
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{calculation(exp)}'\n"
            f"Let's try again, {name}!"
        )


def random_num():
    num_1, num_2 = (
        random.randint(NUM_MIN, NUM_MAX),  # NOSONAR
        random.randint(NUM_MIN, NUM_MAX)  # NOSONAR
    )
    numbers = f'{num_1} {num_2}'
    return numbers


def quest_gcd(numbers):

    print(f'Question: {numbers}')


def calc_gcd(numbers):

    num_1, num_2 = numbers.split(' ')
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        return num_1
    elif num_2 != 0:
        while num_2 != 0:
            temp = num_2
            num_2 = num_1 % num_2
            num_1 = temp
        return temp


def comparison(answer: int, numbers: int, name: str):
    if answer == calc_gcd(numbers):
        print(CORRECT_ANSWER)
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{calc_gcd(numbers)}'\n"
            f"Let's try again, {name}!"
        )


def arithmetic_sequence():
    start = random.randint(NUM_MIN, NUM_MAX)  # NOSONAR
    step = random.randint(STEP_MIN_NUM, STEP_MAX_NUM)  # NOSONAR
    length = random.randint(LENGTH_MIN, LENGTH_MAX)  # NOSONAR
    progression = []
    current_value = start
    for _ in range(length):
        progression.append(current_value)
        current_value += step
    return progression, length


def value(length):
    rndm_value = random.randint(NUM_MIN, length)  # NOSONAR
    return rndm_value


def quest_progression(progression, rndm_value):
    prog = progression.copy()
    prog[rndm_value] = PASS
    print(f'Question: {' '.join([str(i) for i in prog])}')


def calc_progression(rndm_value, progression, name, answer):
    if answer == progression[rndm_value]:
        print(CORRECT_ANSWER)
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{progression[rndm_value]}'\n"
            f"Let's try again, {name}!"
        )


def random_simple():
    numbers = random.randint(NUM_PRIME_MIN, NUM_PRIME_MAX)  # NOSONAR
    print(f'Question: {numbers}')
    return numbers


def square_root(numbers):
    root = int(sqrt(numbers))
    return root


def checking_prime(numbers, root):
    flag = True
    for num in range(2, root):
        if numbers % num == 0:
            flag = False
    return flag


def checking_answer(answer, flag, name):
    if (answer == 'yes' and flag) or (answer == 'no' and not flag):

        print(CORRECT_ANSWER)
        return True
    elif answer == 'yes' and not flag:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was 'no'\n"
            f"Let's try again, {name}!"
        )
    else:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was 'yes'\n"
            f"Let's try again, {name}!"
        )



