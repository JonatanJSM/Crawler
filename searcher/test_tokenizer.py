import unittest
import tokenizer
import os


class TestLanguagesLoadUp(unittest.TestCase):
    def test_tokenizer(self):
        current_dir = os.getcwd()
        json_dir = os.path.join(current_dir, "json")
        archivo_json = os.path.join(json_dir, "languages.json")
        tokenizer.load_accepted_languages(archivo_json)
        self.assertNotEqual(tokenizer.LANGUAGES, [])


class TestInputNormalization(unittest.TestCase):
    def test_tokenizer(self):
        input = "The,.! observant#, @cat"
        response = tokenizer.normalize_input(input)
        self.assertEqual("the observant cat", response)


class TestLanguageRecongnition(unittest.TestCase):
    def test_tokenizer(self):
        current_dir = os.getcwd()
        json_dir = os.path.join(current_dir, "json")
        archivo_json = os.path.join(json_dir, "languages.json")
        input = "The american dream"
        tokenizer.load_accepted_languages(archivo_json)
        response = tokenizer.get_input_language(input)
        self.assertEqual("english", response)


class TestTokenization(unittest.TestCase):
    def test_tokenizer(self):
        current_dir = os.getcwd()
        json_dir = os.path.join(current_dir, "json")
        archivo_json = os.path.join(json_dir, "languages.json")
        input = "El perro podia ver más lejos de su alcance"
        inputMock = dict({"tokens": ["el", "perro", "podia", "ver", "mas", "lejos", "de", "su", "alcance"], "language": "spanish"})
        response = tokenizer.tokenize_input(input, archivo_json)
        self.assertEqual(inputMock, response)


if __name__ == '__main__':
    unittest.main()
