import unittest
import utils.searcher.expander as expander


class TestExpanderWithNoun(unittest.TestCase):
    def test_expander(self):
        wordEs = "auto"
        languageEs = "spanish"
        response = expander.get_similar_matrix(wordEs, languageEs)
        self.assertIsNotNone(response)
        wordEn = "car"
        languageEn = "english"
        response = expander.get_similar_matrix(wordEn, languageEn)
        self.assertIsNotNone(response)


class TestExpanderWithStopWord(unittest.TestCase):
    def test_expander(self):
        wordEs = "el"
        languageEs = "spanish"
        response = expander.get_similar_matrix(wordEs, languageEs)
        self.assertIsNone(response)
        wordEn = "the"
        languageEn = "english"
        response = expander.get_similar_matrix(wordEn, languageEn)
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
