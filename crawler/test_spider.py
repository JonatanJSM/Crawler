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

    def test_is_html(self):
        spider = Spider(2, None)
        self.assertTrue(spider.is_html("text/html"))

    def test_is_not_html(self):
        spider = Spider(2, None)
        self.assertFalse(spider.is_html("application/json"))

    def test_is_sameDomain(self):
        spider = Spider(2, None)
        self.assertTrue(spider.is_sameDomain("http://wagslane.dev", "wagslane.dev"))

    def test_is_not_sameDomain(self):
        spider = Spider(2, None)
        self.assertFalse(spider.is_sameDomain("http://wagslane.dev", "wagslane.com"))

    def test_parse_links(self):
        mock_parse_links = MagicMock()
        spider = Spider(2, None)
        spider.parse_links = mock_parse_links
        spider.parse_links(None, "http://wagslane.dev", 0, "wagslane.dev")
        mock_parse_links.assert_called_once()

    def test_save_item(self):
        mock_save_item = MagicMock()
        spider = Spider(2, None)
        spider.save_item = mock_save_item
        spider.save_item(None, "http://wagslane.dev")
        mock_save_item.assert_called_once()


if __name__ == '__main__':
    unittest.main()
