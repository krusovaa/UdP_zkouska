def load_text():
    """load text to be translated to morse code"""
    while True:
        inp = input('Enter an absolute path to a text file that you want to translate to morse code: ')
        try:
            # load text file into local variable
            with open(inp, 'r', encoding='utf-8-sig') as f:
                text = f.read()
                break
        # exceptions treatment
        except FileNotFoundError:
            print('No such text file.')
            continue
        except PermissionError:
            print('Not adequate access rights.')
            continue
    return text


def encrypt(text):
    """encrypt the text file to morse code and export it to a new text file"""
    cipher = ''
    # change all letters into uppercase letters, which are used in the morse_code_dict_cz
    text_upper = text.upper()
    for letter in text_upper:
        if letter != ' ':
            if letter in morse_code_dict_cz:
                # write morse code for selected letter and a space
                cipher += morse_code_dict_cz[letter] + ' '
            elif letter == '\n':
                cipher += '\n'
            else:
                #  if the character is not in morse_code_dict_cz, nothing is added to a cipher
                cipher += ''
        else:
            cipher += '/ '
    try:
        # export encrypted text to a new text file
        with open('text_to_morse.txt', 'w') as f:
            f.write(cipher)
        # open morse code file and translate each line back into text file
        with open('text_to_morse.txt', 'r') as F:
            text_to_morse_lines = F.readlines()
            for line in text_to_morse_lines:
                decrypt(line)
    # exception treatment
    except PermissionError:
        print('Not adequate access rights.')


def decrypt(morse_cipher):
    """decrypt text given as parameter and export it to a new text file"""
    decipher = ''
    # morse code is split at each space
    morse_cipher_separated = morse_cipher.split(' ')
    for char in morse_cipher_separated:
        if char != ' ':
            if char in inv_morse_code_dict:
                # write a letter for selected morse code characters
                decipher += inv_morse_code_dict[char]
            elif char == '/':
                decipher += ' '
    try:
        # export decrypted text to a new text file
        with open('morse_to_text.txt', 'a+') as f:
            f.write(decipher + '\n')
    # exception treatment
    except PermissionError:
        print('Not adequate access rights.')


# morse code dictionary used for translation from text to morse
morse_code_dict_cz = {
    'A': '.-', 'Á': '.-', 'B': '-...', 'C': '-.-.', 'Č': '-.-.', 'D': '-..', 'Ď': '-..', 'E': '.', 'É': '.', 'Ě': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'Í': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'Ň': '-.', 'O': '---', 'Ó': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'Ř': '.-.', 'S': '...',
    'Š': '...', 'T': '-', 'Ť': '-', 'U': '..-', 'Ú': '..-', 'Ů': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Ý': '-.--', 'Z': '--..', 'Ž': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.', '?': '..--..', '/': '-..-.'}

# morse code dictionary used for translation from morse to text
morse_code_dict_int = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.', '?': '..--..', '/': '-..-.'}

# getting keys using values
inv_morse_code_dict = dict((v, k) for (k, v) in morse_code_dict_int.items())

# running function
encrypt(load_text())
