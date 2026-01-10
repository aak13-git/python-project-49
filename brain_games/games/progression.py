from brain_games.common.utils import (
    arithmetic_sequence,
    calc_progression,
    get_name,
    greet,
    quest_progression,
    value,
    welcome,
)


def brain_progression():
    welcome()
    name = get_name()
    greet(name)

    print('What number is missing in the progression?')

    total = 0
    for _ in range(3):
        progression, length = arithmetic_sequence()
        rndm_value = value(length)
        quest_progression(progression, rndm_value)
        answer = int(input('Your answer: '))
        if calc_progression(rndm_value, progression, name, answer):
            total += 1
        else:
            break

    if total == 3:
        print(f'Congratulations, {name}!')