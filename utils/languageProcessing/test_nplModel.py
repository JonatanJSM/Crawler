import unittest
from utils.languageProcessing.nplModel import (
    preprocess, get_lis_stopwords, get_words,
    get_words_without_stopwords, get_words_lemanized,
    get_words_stemmed
)


class TestNplModel(unittest.TestCase):
    def test_preprocess(self):
        text = "This is a test sentence."
        self.assertEqual(preprocess(text), "test sentenc")

    def test_preprocess_empty_string(self):
        text = ""
        self.assertEqual(preprocess(text), "")

    def test_preprocess_special_characters(self):
        text = "This is a test sentence with special characters!@#$%^&*()_+"
        self.assertNotEqual(preprocess(text), "test sentenc special charact")

    def test_get_lis_stopwords(self):
        word = {"in", "the", "and", "or", "is", "a", "an", "to", "for", "of", "on", "at", "by", "with", "about", "as"}
        self.assertTrue(get_lis_stopwords().issuperset(word))

    def test_get_lis_stopwords_not_empty(self):
        self.assertTrue(len(get_lis_stopwords()) > 0)

    def test_get_words(self):
        text = "This is a test sentence"
        self.assertEqual(get_words(text), ['this', 'is', 'a', 'test', 'sentence'])

    def test_get_words_empty_string(self):
        text = ""
        self.assertEqual(get_words(text), [])

    def test_get_words_without_stopwords(self):
        text = ['this', 'is', 'a', 'test', 'sentence']
        stop_words = {"this", "is", "a"}
        self.assertEqual(get_words_without_stopwords(text, stop_words), ['test', 'sentence'])

    def test_get_words_without_stopwords_empty_string(self):
        text = []
        stop_words = {"this", "is", "a"}
        self.assertEqual(get_words_without_stopwords(text, stop_words), [])

    def test_get_words_lemanized(self):
        text = ['test', 'sentence']
        self.assertEqual(get_words_lemanized(text), ['test', 'sentence'])

    def test_get_words_lemanized_empty_string(self):
        text = []
        self.assertEqual(get_words_lemanized(text), [])

    def test_get_words_stemmed(self):
        text = ['test', 'sentence']
        self.assertEqual(get_words_stemmed(text), ['test', 'sentenc'])

    def test_get_words_stemmed_empty_string(self):
        text = []
        self.assertEqual(get_words_stemmed(text), [])
