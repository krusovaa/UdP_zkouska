import itertools
import string


def get_char():
    lowers = list(string.ascii_lowercase)
    uppers = list(string.ascii_uppercase)
    numbers = [str(i) for i in range(1, 10)]
    all_char = lowers + uppers + numbers
    return all_char


def input_length():
    print('How long do you want your password combinations to be?')
    while True:
        inp = input('Enter an integer between 2 and 6: ')
        try:
            inp = int(inp)
        except ValueError:
            print('Invalid integer.')
            continue
        if 2 <= inp <= 6:
            break
        else:
            print('Invalid range.')
    return inp


def pw_gen(characters, length):
    with open("password_combinations.txt", "a+") as f:
        #comb_list = []
        for i in itertools.product(characters, repeat=length):
            combination = ''.join(i)
            f.write(combination)
            f.write('\n')

pw_gen(get_char(), input_length())
