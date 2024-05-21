from core.utils.languageProcessing.nplModel import use_classifier
import os


class Item:
    def __init__(self, title, metaTitle, metaType, metaDescription, url, category):
        self.__title = title
        self.__metaTitle = metaTitle
        self.__metaType = metaType
        self.__metaDescription = metaDescription
        self.__url = url
        self.__category = category

    @staticmethod
    def validate_meta_elements(metaTitle, metaType, metaDescription):
        if metaTitle is None or metaType is None or metaDescription is None:
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
    def __create_category(text):
        current_dir = os.getcwd()
        path = os.path.join(current_dir, 'core', 'utils', 'languageProcessing')
        category = text
        categoryNew = use_classifier(category, path)
        return categoryNew

    @classmethod
    def create_item(cls, soup_html, url):
        title = soup_html.title.text.strip()
        metaTitle = soup_html.find("meta", property="og:title")
        metaType = soup_html.find("meta", property="og:type")
        metaDescription = soup_html.find("meta", property="og:description")

        if not cls.validate_meta_elements(metaTitle, metaType, metaDescription):
            return None

        text1 = cls.clean_html_text(soup_html)
        text2 = cls.systematic_sampling(text1)
        category = cls.__create_category(text2)
        return cls(title, metaTitle["content"], metaType["content"], metaDescription["content"], url, category)

    def __str__(self):
        return f"Item: {self.__title}, {self.__metaTitle}, {self.__metaType}, {self.__metaDescription}, {self.__url}, {self.__metaTitlecategory}"

    def __json__(self):
        return {
            "title": self.__title,
            "metaTitle": self.__metaTitle,
            "metaType": self.__metaType,
            "metaDescription": self.__metaDescription,
            "url": self.__url,
            "category": self.__category
        }

    def get_title(self):
        return self.__title

    def get_metaTitle(self):
        return self.__metaTitle

    def get_metaType(self):
        return self.__metaType

    def get_metaDescription(self):
        return self.__metaDescription

    def get_url(self):
        return self.__url

    def get_category(self):
        return self.__category
