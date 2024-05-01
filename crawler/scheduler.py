from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser


class Scheduler:
    def __init__(self):
        self.queue = []
        self.robot_parser = RobotFileParser()

    def enqueue_request(self, request):
        domain = urlparse(request.url).netloc

        robot_url = f"http://{domain}/robots.txt"

        try:
            self.robot_parser.set_url(robot_url)
            self.robot_parser.read()
        except Exception as e:
            print(f"No se pudo obtener el archivo robots.txt para {domain}: {e}")
            return

        if not self.robot_parser.can_fetch("*", request.url):
            print(f"Solicitud denegada por robots.txt: {request.url}")
            return

        self.queue.append(request)

    def next_request(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None
