from brain_games.common.utils import welcome, get_name, greet, arithmetic_sequence, quest_progression, calc_progression, \
    value


def brain_progression():
    welcome()
    name = get_name()
    greet(name)

    print('What number is missing in the progression?')

    total = 0
    for quest in range(3):
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


def main():

    brain_progression()


if __name__ == "__main__":
    main()

