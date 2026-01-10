from brain_games.common.utils import (
    calc_gcd,
    comparison,
    get_name,
    greet,
    quest_gcd,
    random_num,
    welcome,
)


def brain_gcd():
    welcome()
    name = get_name()
    greet(name)

    print('Find the greatest common divisor of given numbers.')

    total = 0
    for quest in range(3):
        numbers = random_num()
        calc_gcd(numbers)
        quest_gcd(numbers)
        answer = int(input('Your answer: '))
        if comparison(answer, numbers, name):
            total += 1
        else:
            break

    if total == 3:

        print(f'Congratulations, {name}!')