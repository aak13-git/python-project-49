from brain_games.common.utils import welcome, get_name, greet, random_num, calc_gcd, comparison, quest_gcd


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


def main():

    brain_gcd()


if __name__ == "__main__":
    main()