# import modules
import itertools
import string


def get_char():
    """create list of characters from which the combinations of password are going to be made of"""
    # list of lowercase characters
    lowers = list(string.ascii_lowercase)
    # list of uppercase characters
    uppers = list(string.ascii_uppercase)
    # list of numbers
    numbers = [str(i) for i in range(1, 10)]
    all_char = lowers + uppers + numbers
    print(len(all_char))
    return all_char


def input_length():
    """check the right input of the length of the password"""
    print('How long do you want your password combinations to be?')
    while True:
        inp = input('Enter an integer between 2 and 6: ')
        try:
            # check the right type of input (integer)
            inp = int(inp)
        # exception treatment
        except ValueError:
            print('Invalid integer.')
            continue
        # check the input in the right range (2 - 6)
        if 2 <= inp <= 6:
            break
        else:
            print('Invalid range.')
    return inp


def pw_gen(characters, length):
    """generate all characters combinations with selected length and export them to a text file"""
    try:
        # output text file
        with open("password_combinations.txt", "a+") as f:
            for p in itertools.product(characters, repeat=length):
                combination = ''.join(p)
                # write each combination and create a new line
                f.write(combination + '\n')
    # exception treatment
    except PermissionError:
        print('Not adequate access rights: ', f)


pw_gen(get_char(), input_length())
