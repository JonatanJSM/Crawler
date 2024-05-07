import unittest
from core.repository.scheduler import Scheduler
from core.entity.request import Request
from unittest.mock import MagicMock


class TestScheduler(unittest.TestCase):
    def test_enqueue_request(self):
        scheduler = Scheduler()
        urls = ["https://www.wagslane.dev/"]
        scheduler.enqueue_request(Request(urls[0]))
        self.assertEqual(len(scheduler.queue), 1)

    def test_next_request(self):
        scheduler = Scheduler()
        urls = ["https://www.wagslane.dev/"]
        scheduler.enqueue_request(Request(urls[0]))
        self.assertEqual(scheduler.next_request().url, urls[0])

    def test_next_request_empty_queue(self):
        scheduler = Scheduler()
        self.assertEqual(scheduler.next_request(), None)

    def test_next_request_mocked(self):
        scheduler = Scheduler()
        urls = ["https://www.wagslane.dev/"]
        enqueue_request = MagicMock()
        scheduler.enqueue_request = enqueue_request
        scheduler.enqueue_request(Request(urls[0]))
        scheduler.enqueue_request.assert_called_once()


if __name__ == '__main__':
    unittest.main()
