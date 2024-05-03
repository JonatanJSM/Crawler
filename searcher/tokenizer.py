from unidecode import unidecode
from nltk.tokenize import RegexpTokenizer
import langid


def normalize_input(userInput):
    normalizedInput = unidecode(userInput)
    normalizedInput = ''.join(letter for letter in normalizedInput if letter.isalnum() or letter == " ")
    return normalizedInput.lower()


def get_input_language(word):
    lang = langid.classify(word)
    language = ""
    if lang[0] == "en":
        language = "english"
    if lang[0] == "es" or lang[0] == "it":
        language = "spanish"
    return language


def tokenize_input(userInput):
    cleanInput = normalize_input(userInput)
    language = get_input_language(cleanInput)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(cleanInput)
    tokenDict = dict({"tokens": tokens, "language": language})
    return tokenDict
