import random


def brain_even():

    print("Welcome to the Brain Games!")

    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no"')

    total = 0
    for quest in range(3):
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if question % 2 != 0 and (answer == 'yes' or answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'\nLet's try again, {name}!")
            break

        elif question % 2 == 0 and (answer == 'no' or answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'\nLet's try again, {name}!")
            break

        elif question % 2 == 0 and answer == 'yes' or question % 2 != 0 and answer == 'no':
            print('Correct!')
            total += 1
            continue
    if total == 3:
        print(f'Congratulations, {name}!')


def main():

    brain_even()


if __name__ == "__main__":
    main()

