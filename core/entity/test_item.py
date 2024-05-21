import unittest
from core.entity.item import Item
from bs4 import BeautifulSoup


class TestItem(unittest.TestCase):
    def test_item(self):
        item = Item("title", "metaTitle", "metaType", "metaDescription", "url", "category")
        self.assertEqual(item.get_title(), "title")
        self.assertEqual(item.get_metaTitle(), "metaTitle")
        self.assertEqual(item.get_metaType(), "metaType")
        self.assertEqual(item.get_metaDescription(), "metaDescription")
        self.assertEqual(item.get_url(), "url")
        self.assertEqual(item.get_category(), "category")

    def test_validate_meta_elements(self):
        self.assertTrue(Item.validate_meta_elements("metaTitle", "metaType", "metaDescription"))
        self.assertFalse(Item.validate_meta_elements(None, "metaType", "metaDescription"))

    def test_clean_html_text(self):
        html = "<html><body><p>Test</p></body></html>"
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEqual(Item.clean_html_text(soup), "Test")

    def test_systematic_sampling(self):
        text = "sentence1, sentence2, sentence3"
        self.assertEqual(Item.systematic_sampling(text), "sentence1")

    def test_create_item(self):
        html = '''<html><head><title>Test</title>
        <meta property='og:title' content='metaTitle'>
        <meta property='og:type' content='metaType'>
        <meta property='og:description' content='metaDescription'>
        </head></html>'''
        soup = BeautifulSoup(html, 'html.parser')
        item = Item.create_item(soup, "url")
        self.assertEqual(item.get_title(), "Test")
        self.assertEqual(item.get_metaTitle(), "metaTitle")
        self.assertEqual(item.get_metaType(), "metaType")
        self.assertEqual(item.get_metaDescription(), "metaDescription")
        self.assertEqual(item.get_url(), "url")
        self.assertEqual(item.get_category(), "Programming")


if __name__ == '__main__':
    unittest.main()
