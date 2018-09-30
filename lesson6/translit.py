tabl = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
        "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
        "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
        "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
        "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "\'",
        "б": "b", "ю": "ju", "ё": "jo"
        }
text = open('cyrillic.txt', encoding='utf8').read().split('\n')
# text = input().split('\n')
newFile = open('transliteration.txt', 'w', encoding='utf8')


for line in text:
    newLine = []

    for letter in line:
        if not letter.isalpha() or 64 < ord(letter) < 91 or 96 < ord(letter) < 123:
            newLine.append(letter)
            continue

        isUpper = letter.isupper()
        newLetter = tabl[letter.lower()]
        newLine.append(newLetter[0].upper() + newLetter[1:] if isUpper else newLetter)

    print(''.join(newLine), file=newFile)

newFile.close()
