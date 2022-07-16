import random


def get_number():
    while True:
        try:
            result = int(input("Chose the number: "))
            break
        except ValueError:
            print("It is not a number")

    return result


def get_numbers():
    result = []
    while len(result) < 6:
        number = get_number()
        if number not in result and 0 < number <= 49:
            result.append(number)

    return result


def print_numbers(numbers):

    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    user_numbers = get_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
