import unittest
from crawler.request import Request
from crawler.downloader import Downloader


class TestDownloader(unittest.TestCase):
    def test_download(self):
        urls = ["https://www.wagslane.dev/"]
        request = Request(urls[0])
        downloader = Downloader()
        response = downloader.download(request)
        self.assertEqual(response.status_code, 200)


class TestDownloaderFail(unittest.TestCase):
    def test_download(self):
        urls = ["https://www.wa"]
        request = Request(urls[0])
        downloader = Downloader()
        response = downloader.download(request)
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
