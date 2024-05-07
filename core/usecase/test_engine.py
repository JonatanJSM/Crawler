import unittest
from core.usecase.engine import Engine
from unittest.mock import MagicMock


class TestEngine(unittest.TestCase):

    def test_engine_start_called(self):
        urls = ["https://www.wagslane.dev/"]
        engine = Engine(urls)
        mock_start = MagicMock()
        engine.start = mock_start
        engine.start()
        mock_start.assert_called_once()

    def test_enqueue_request(self):
        urls = ["https://www.wagslane.dev/"]
        engine = Engine(urls)
        engine.start()
        assert len(engine.scheduler.queue) == 0


if __name__ == '__main__':
    unittest.main()
