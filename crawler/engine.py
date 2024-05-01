from crawler.request import Request
from crawler.scheduler import Scheduler
from crawler.downloader import Downloader
from crawler.spider import Spider


class Engine:
    def __init__(self, ulrs, max_depth=2):
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.spider = Spider(max_depth, self.scheduler)
        self.urls = ulrs

    def start(self):
        for self.url in self.urls:
            request = Request(self.url)
            self.scheduler.enqueue_request(request)
            while True:
                request = self.scheduler.next_request()
                if not request:
                    break
                response = self.downloader.download(request)
                if response:
                    self.spider.parse(response, request.depth, request.domain)
