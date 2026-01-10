from brain_games.common.utils import (
    get_name,
    greet,
    num_even,
    quest_even,
    welcome,
)


def brain_even():
    welcome()
    name = get_name()
    greet(name)

    print('Answer "yes" if the number is even, otherwise answer "no"')

    total = 0
    for _ in range(3):
        num = num_even()
        quest_even(num)
        answer = input('Your answer: ')
        if num % 2 != 0 and (answer == 'yes' or answer != 'no'):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was 'no'\n"
                f"Let's try again, {name}!"
            )
            break

        elif (
            num % 2 == 0
            and (answer == 'no' or answer != 'yes')
        ):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was 'yes'\n"
                f"Let's try again, {name}!"
            )
            break

        elif (
            num % 2 == 0 and answer == 'yes'
            or num % 2 != 0 and answer == 'no'
        ):
            print('Correct!')
            total += 1
    if total == 3:

        print(f'Congratulations, {name}!')