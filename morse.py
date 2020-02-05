# Morseovka:
# Ze vstupního souboru načtěte text,  zkonvertujete ho na Morseovu abecedu a uložte do souboru.
# Následně tento soubor zpětně překonvertujte opět na text.

# C:\Users\zvukar\Desktop\B 4. ročník\Úvod do programování\uvodoprogram.txt


def load_text():
    q = input("Zadej absoutní adresu textového souboru, který chceš převézt na morseovku: ")
    with open(q, 'r+', encoding='utf-8-sig') as f:
        text = f.read()
    print(text)
    return text


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
    with open('text_to_morse.txt', 'w+') as f:
        f.write(cipher)


# def decrypt(message):
#     message += ' '
#     decipher = ''
#     citext = ''
#     for letter in message:
#         if letter != ' ':
#             i = 0
#             citext += letter
#         else:
#             i += 1
#             if i == 2:
#                 decipher += ' '
#                 decipher += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(citext)]
#                 citext = ''
#     return decipher


morse_code_dict = {
    'A': '.-', 'Á': '.-', 'B': '-...', 'C': '-.-.', 'Č': '-.-.',
    'D': '-..', 'Ď': '-..', 'E': '.', 'É': '.', 'Ě': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'Í': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'Ň': '-.', 'O': '---', 'Ó': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'Ř': '.-.', 'S': '...', 'Š': '...', 'T': '-',
    'Ť': '-', 'U': '..-', 'Ú': '..-', 'Ů': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Ý': '-.--', 'Z': '--..', 'Ž': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.*': '.-.-.-', ',': '--..--', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

encrypt(load_text())
