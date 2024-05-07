from unidecode import unidecode
from nltk.tokenize import RegexpTokenizer
from googletrans import Translator
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
    translator = Translator()
    lang = translator.detect(word)
    language = "notFound"
    for possibleLanguage in LANGUAGES:
        if str(lang.lang) == possibleLanguage.get("abbreviation"):
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
