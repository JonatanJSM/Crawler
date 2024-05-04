from languageProcessing.nplModel import use_classifier
import os


class Item:
    def __init__(self, title, metaTitle, metaType, metaDescription, url, category):
        self.title = title
        self.metaTitle = metaTitle
        self.metaType = metaType
        self.metaDescription = metaDescription
        self.url = url
        self.category = category

    @staticmethod
    def validate_meta_elements(metaTitle, metaType, metaDescription):
        if metaTitle is None or metaType is None or metaDescription is None:
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
    def systematic_sampling(text):
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
    def create_item(cls, soup_html, url):
        title = soup_html.title.text.strip()
        metaTitle = soup_html.find("meta", property="og:title")
        metaType = soup_html.find("meta", property="og:type")
        metaDescription = soup_html.find("meta", property="og:description")
        category = "prueba"

        if not cls.validate_meta_elements(metaTitle, metaType, metaDescription):
            return None

        text1 = cls.clean_html_text(soup_html)
        text2 = cls.systematic_sampling(text1)
        category = cls.create_category(text2)
        return cls(title, metaTitle["content"], metaType["content"], metaDescription["content"], url, category)

    def __str__(self):
        return f"Item: {self.title}, {self.metaTitle}, {self.metaType}, {self.metaDescription}, {self.url}, {self.category}"

    def __json__(self):
        return {
            "title": self.title,
            "metaTitle": self.metaTitle,
            "metaType": self.metaType,
            "metaDescription": self.metaDescription,
            "url": self.url,
            "category": self.category
        }
