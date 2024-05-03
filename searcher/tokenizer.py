from unidecode import unidecode
from nltk.tokenize import RegexpTokenizer
import langid
import json


LANGUAGES = []


def load_accepted_languages(path):
    f = open(path)
    data = json.load(f)
    global LANGUAGES
    LANGUAGES = data["acceptedLanguages"]
    f.close()


def normalize_input(userInput):
    normalizedInput = unidecode(userInput)
    normalizedInput = ''.join(letter for letter in normalizedInput if letter.isalnum() or letter == " ")
    return normalizedInput.lower()


def get_input_language(word):
    lang = langid.classify(word)
    language = ""
    for possibleLanguage in LANGUAGES:
        if lang[0] == possibleLanguage.get("abbreviation"):
            language = possibleLanguage.get("language")
            break
    return language


def tokenize_input(userInput, path):
    load_accepted_languages(path)
    cleanInput = normalize_input(userInput)
    language = get_input_language(cleanInput)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(cleanInput)
    tokenDict = dict({"tokens": tokens, "language": language})
    return tokenDict
