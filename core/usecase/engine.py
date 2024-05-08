from core.entity.request import Request
from core.usecase.scheduler import Scheduler
from core.usecase.downloader import Downloader
from core.usecase.spider import Spider
import traceback


class Engine:
    def __init__(self, ulrs, max_depth=0, core_name="v2", solrClientManager=None):
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.spider = Spider(max_depth, self.scheduler, solrClientManager)
        self.urls = [ulrs]
        self.core_name = core_name

    def start(self):
        try:
            for url in self.urls:
                request = Request(url)
                self.scheduler.enqueue_request(request)
                while True:
                    request = self.scheduler.next_request()
                    if not request:
                        break
                    response = self.downloader.download(request)
                    print("Se está bajando la", request.url)
                    if response:
                        self.spider.parse(response, request.depth, request.domain, self.core_name)
        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
            return False
        else:
            return True
