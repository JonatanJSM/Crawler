from languageProcessing.nplModel import use_classifier
import os


class Item:
    def __init__(self, title, meta_title, meta_type, meta_description, page_url, category):
        self.title = title
        self.meta_title = meta_title
        self.meta_type = meta_type
        self.meta_description = meta_description
        self.page_url = page_url
        self.category = category

    @staticmethod
    def validate_meta_elements(meta_title, meta_type, meta_description):
        if meta_title is None or meta_type is None or meta_description is None:
            print("Alguno de los elementos requeridos está ausente.")
            return False
        else:
            return True

    @staticmethod
    def clean_html_text(soup_html):
        soup = soup_html

        for data in soup(['style', 'script']):
            data.decompose()
        return ' '.join(soup.stripped_strings)

    @staticmethod
    def systematic_sampling(text, sample_size):
        sentences = text.split(',')
        step_size = len(sentences)
        sampled_sentences = [sentences[i] for i in range(0, len(sentences), step_size)]
        sampled_text = ' '.join(sampled_sentences)
        return sampled_text

    @staticmethod
    def create_category(text):
        current_dir = os.getcwd()
        path = os.path.join(current_dir, 'languageProcessing')
        category = text
        categoryNew = use_classifier(category, path)
        print(f"La categoría es: {category}")
        return categoryNew

    @classmethod
    def create_item(cls, soup_html, page_url):
        title = soup_html.title.text.strip()
        meta_title = soup_html.find("meta", property="og:title")
        meta_type = soup_html.find("meta", property="og:type")
        meta_description = soup_html.find("meta", property="og:description")
        category = "prueba"

        if not cls.validate_meta_elements(meta_title, meta_type, meta_description):
            return None

        text1 = cls.clean_html_text(soup_html)
        text2 = cls.systematic_sampling(text1, 5)
        category = cls.create_category(text2)
        return cls(title, meta_title["content"], meta_type["content"], meta_description["content"], page_url, category)

    def __str__(self):
        return f"Item: {self.title}, {self.meta_title}, {self.meta_type}, {self.meta_description}, {self.page_url}, {self.category}"
