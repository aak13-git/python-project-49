from brain_games.common.utils import (
    calculation,
    exp_calc,
    get_name,
    greet,
    quest_calc,
    result,
    welcome,
)


def brain_calc():
    welcome()
    name = get_name()
    greet(name)

    print('What is the result of the expression?')

    total = 0
    for quest in range(3):
        exp = exp_calc()
        quest_calc(exp)
        answer = int(input('Your answer: '))
        calculation(exp)
        if result(answer, name, exp):
            total += 1
        else:
            break

    if total == 3:

        print(f'Congratulations, {name}!')


def main():

    brain_calc()


if __name__ == "__main__":
    main()




