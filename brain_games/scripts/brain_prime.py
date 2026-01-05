from brain_games.common.utils import welcome, get_name, greet, random_simple, square_root, checking_prime, \
    checking_answer


def brain_prime():
    welcome()
    name = get_name()
    greet(name)

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    total = 0

    for quest in range(3):
        numbers = random_simple()
        root = square_root(numbers)
        answer = input('Your answer: ')
        flag = checking_prime(numbers, root)
        if checking_answer(answer, flag, name):
            total += 1
        else:
            break

    if total == 3:
        print(f'Congratulations, {name}!')


def main():

    brain_prime()


if __name__ == "__main__":
    main()




