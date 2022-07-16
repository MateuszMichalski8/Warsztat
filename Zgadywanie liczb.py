import random


def get_number():
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It is not a number")

    return result


def guess_number():
    number = random.randint(1, 100)
    given_number = get_number()
    while given_number != number:
        if given_number < number:
            print("Too small!")
        else:
            print("Too Big")
        given_number = get_number()
    print("You Win!")

if __name__ == '__main__':
    guess_number()
