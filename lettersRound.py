from numpy import random
import lettersDict

vowels = ['A', 'E', 'I', 'O', 'U']
consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def generateConsonant():
    return random.choice(consonant, 1, p=[2/62.79, 4/62.79, 3.8/62.79, 1.4/62.79, 3/62.79,
                                          2.3/62.79, .21/62.79, .97/62.79, 5.3/62.79, 2.7/62.79,
                                          7.2/62.79, 2.8/62.79, .19/62.79, 7.3/62.79, 8.7/62.79,
                                          6.7/62.79, 1/62.79, .91/62.79, .27/62.79, 1.6/62.79, 
                                          0.44/62.79])[0]

def generateVowel():
    return random.choice(vowels, 1, p=[7.8/36.8, 11/36.8, 8.6/36.8, 6.1/36.8, 3.3/36.8])[0]

def generateLetter(letters, choice, VOWEL_MIN = 3, VOWEL_MAX = 5, LETTERS_MAX = 9):
    vowel_count = getVowelCount(letters)
    if(LETTERS_MAX - len(letters) == VOWEL_MIN - vowel_count):
        letters.append(generateVowel())
    elif(VOWEL_MAX == vowel_count):
        letters.append(generateConsonant())
    else:
        if(choice == 'V'):
            letters.append(generateVowel())
        elif(choice == 'C'):
            letters.append(generateConsonant())
    return letters

def getVowelCount(letters : list):
    vowel_count = 0
    for letter in letters:
        if (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
            vowel_count += 1
    return vowel_count

print(generateConsonant())

# letters = []
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'V')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# letters = generateLetter(letters, 'C')
# print(letters)
# print(lettersDict.findLongestWord(letters))