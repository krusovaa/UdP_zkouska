def load_text():
    while True:
        inp = input('Enter an absolute path to a text file that you want to translate to morse code: ')
        try:
            with open(inp, 'r', encoding='utf-8-sig') as f:
                text = f.read()
                break
        except FileNotFoundError:
            print('No such text file.')
            continue
        except PermissionError:
            print('Not adequate access rights.')
            continue
    return text


def encrypt(text):
    cipher = ''
    text_upper = text.upper()
    for letter in text_upper:
        if letter != ' ':
            if letter in morse_code_dict_cz:
                cipher += morse_code_dict_cz[letter] + ' '
            elif letter == '\n':
                cipher += '\n'
            else:
                #  character not in morse_code_dict_cz
                cipher += ''
        else:
            cipher += '/ '
    try:
        with open('text_to_morse.txt', 'w') as f:
            f.write(cipher)
        with open('text_to_morse.txt', 'r') as F:
            text_to_morse_lines = F.readlines()
            for line in text_to_morse_lines:
                decrypt(line)
    except PermissionError:
        print('Not adequate access rights.')


def decrypt(morse_cipher):
    decipher = ''
    morse_cipher_separated = morse_cipher.split(' ')
    for char in morse_cipher_separated:
        if char != ' ':
            if char in inv_morse_code_dict:
                decipher += inv_morse_code_dict[char]
            elif char == '/':
                decipher += ' '
    try:
        with open('morse_to_text.txt', 'a+') as f:
            f.write(decipher + '\n')
    except PermissionError:
        print('Not adequate access rights.')


morse_code_dict_cz = {
    'A': '.-', 'Á': '.-', 'B': '-...', 'C': '-.-.', 'Č': '-.-.', 'D': '-..', 'Ď': '-..', 'E': '.', 'É': '.', 'Ě': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'Í': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'Ň': '-.', 'O': '---', 'Ó': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'Ř': '.-.', 'S': '...',
    'Š': '...', 'T': '-', 'Ť': '-', 'U': '..-', 'Ú': '..-', 'Ů': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Ý': '-.--', 'Z': '--..', 'Ž': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.', '?': '..--..', '/': '-..-.'}

morse_code_dict_int = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.', '?': '..--..', '/': '-..-.'}

inv_morse_code_dict = dict((v, k) for (k, v) in morse_code_dict_int.items())

encrypt(load_text())
