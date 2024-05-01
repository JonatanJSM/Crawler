import unittest
from crawler.scheduler import Scheduler
from crawler.request import Request


class TestScheduler(unittest.TestCase):
    def test_enqueue_request(self):
        scheduler = Scheduler()
        urls = ["https://www.wagslane.dev/"]
        scheduler.enqueue_request(Request(urls[0]))
        self.assertEqual(len(scheduler.queue), 1)


if __name__ == '__main__':
    unittest.main()
