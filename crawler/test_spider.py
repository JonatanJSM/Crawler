import unittest
from crawler.spider import Spider
from crawler.request import Request
from crawler.downloader import Downloader
from unittest.mock import MagicMock


class TestSpider(unittest.TestCase):
    def test_parse(self):
        mock_parse = MagicMock()
        request = Request("http://wagslane.dev")
        downloader = Downloader()
        response = downloader.download(request)
        spider = Spider(2, None)
        spider.parse = mock_parse
        spider.parse(response, 0, "wagslane.dev")
        mock_parse.assert_called_once()

    def test_create_item(self):
        mock_create_item = MagicMock()
        spider = Spider(2, None)
        spider.create_item = mock_create_item
        spider.create_item(None, "http://wagslane.dev")
        mock_create_item.assert_called_once()


if __name__ == '__main__':
    unittest.main()
