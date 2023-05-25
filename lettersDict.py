import requests
from numpy import random

base_api = "https://api.dictionaryapi.dev/api/v2/entries/en/"

anagram_api = "http://www.anagramica.com/best/:"

def checkWordExists(word):
    response = requests.get(base_api + word).json()
    if(type(response) == type([])):
        return True
    else:
        return False

def checkValidWord(letters, word):
    for letter in word:
        if(not (letter in letters)):
            return False
    return True

def findLongestWord(letters):
    word = ""
    for letter in letters:
        word += letter
    response = requests.get(anagram_api + word).json()
    listOfLongest = response.get('best')
    if (len(listOfLongest)) :
        return listOfLongest[random.randint(0, len(listOfLongest))]
    else:
        return None