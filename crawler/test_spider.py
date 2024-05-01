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


if __name__ == '__main__':
    unittest.main()
