# Morseovka:
# Ze vstupního souboru načtěte text,  zkonvertujete ho na Morseovu abecedu a uložte do souboru.
# Následně tento soubor zpětně překonvertujte opět na text.

# C:\Users\zvukar\Desktop\B 4. ročník\Úvod do programování\uvodoprogram.txt


def load_text():
    q = input("Zadej absoutní adresu textového souboru, který chceš převézt na morseovku: ")
    f = open(q, 'r+', encoding='utf-8')
    text = f.read()
    f.close()
    # print(text)


def encrypt(text):
    cipher = ''
    text_upper = text.upper()  # kapitalky
    for letter in text_upper:
        if letter != ' ':
            if letter in morse_code_dict:
                cipher += morse_code_dict[letter] + ' '
            else:
                cipher += letter
        else:
            cipher += '/'
    print(cipher)


def decrypt():
    pass


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.*': '.-.-.-', ',': '--..--', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-'}

encrypt('ahoj, jak se máš? . com')
