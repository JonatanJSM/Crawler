from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser


class Scheduler:
    def __init__(self):
        self.__queue = []
        self.__robot_parser = RobotFileParser()

    def enqueue_request(self, request):
        domain = urlparse(request.get_url()).netloc

        robot_url = f"http://{domain}/robots.txt"
        try:
            self.__robot_parser.set_url(robot_url)
            self.__robot_parser.read()
        except Exception as e:
            print(f"No se pudo obtener el archivo robots.txt para {domain}: {e}")
            return

        if not self.__robot_parser.can_fetch("*", request.get_url()):
            print(f"Solicitud denegada por robots.txt: {request.get_url()}")
            return
        self.__queue.append(request)

    def next_request(self):
        if self.__queue:
            return self.__queue.pop(0)
        else:
            return None

    def get_queue(self):
        return self.__queue
