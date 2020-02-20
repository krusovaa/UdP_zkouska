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
    """generate all characters variations with selected length and export them to a text file"""
    # counting number of variations according to a formula in documentation
    k = length
    n = len(characters)
    comb_numb = n ** k

    x = 0
    # first value
    next_percent = 5
    # step of percent done to display
    percent_step = 5
    # 'step' % of combinations
    try:
        # output text file
        with open("password_combinations.txt", "a+") as f:
            for p in itertools.product(characters, repeat=length):
                variation = ''.join(p)
                # write each variation and create a new line
                f.write(variation + '\n')
                x += 1
                # count current percent of computed variations
                percent = 100.0 * x / comb_numb
                if percent >= next_percent:
                    print(f"{next_percent} % complete")
                    # add percent_step
                    while next_percent < percent:
                        next_percent += percent_step
    # exception treatment
    except PermissionError:
        print('Not adequate access rights: ', f)


# running function
pw_gen(get_char(), input_length())
