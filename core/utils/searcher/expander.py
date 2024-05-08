from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


def get_similar_matrix(noun, language):
    array = []
    if noun in stopwords.words(language):
        return None
    langAbrv = language[0:3]
    response = wn.synonyms(noun, lang=langAbrv)
    if len(response) == 0:
        return [noun]
    else:
        for word in response:
            array.append(word)
        array[0].append(noun)
    return array[0]
