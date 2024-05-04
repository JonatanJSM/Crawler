import unittest
from crawler.itemPipeline import itemPipeline
from crawler.item import Item


class TestItemPipeline(unittest.TestCase):

    itemToTest = Item(
        "https://www.wagslane.dev",
        "Wagslane",
        "Wagslane Blog",
        "Wagslane Blog",
        "2021-07-01",
        "Wagslane Blog")

    def test_save_item(self):
        item_pipeline = itemPipeline()
        assert item_pipeline.save_item(self.itemToTest) == self.itemToTest


if __name__ == '__main__':
    unittest.main()
