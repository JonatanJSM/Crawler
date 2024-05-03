import unittest
import tokenizer


class TestInputNormalization(unittest.TestCase):
    def test_tokenizer(self):
        input = "The,.! observant#, @cat"
        response = tokenizer.normalize_input(input)
        self.assertEqual("the observant cat", response)


class TestLanguageRecongnition(unittest.TestCase):
    def test_tokenizer(self):
        input = "The american dream"
        response = tokenizer.get_input_language(input)
        self.assertEqual("english", response)


class TestTokenization(unittest.TestCase):
    def test_tokenizer(self):
        input = "El perro podia ver más lejos de su alcance"
        inputMock = dict({"tokens": ["el", "perro", "podia", "ver", "mas", "lejos", "de", "su", "alcance"], "language": "spanish"})
        response = tokenizer.tokenize_input(input)
        self.assertEqual(inputMock, response)


if __name__ == '__main__':
    unittest.main()
