import unittest
from crawler.itemPipeline import itemPipeline
from crawler.item import Item


class TestItemPipeline(unittest.TestCase):

    itemToTest = Item(
        "Este es el título de la página",
        "meta titulo",
        "html",
        "Este es la descripción de la página",
        "https://wagslane.com/",
        "Blog")

    def test_save_item(self):
        item_pipeline = itemPipeline()
        self.assertEqual(item_pipeline.save_item(self.itemToTest, core="v2"), 200)


if __name__ == '__main__':
    unittest.main()
