from urllib.parse import urlparse


class Request:
    def __init__(self, url, depth=0):
        self.__url = self.__normalize_url(url)
        self.__depth = depth
        self.__domain = self.__extract_domain(url)

    def __extract_domain(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc

    def __normalize_url(self, url):
        if url.endswith('/'):
            return url
        else:
            return url + '/'

    def get_url(self):
        return self.__url

    def get_depth(self):
        return self.__depth

    def get_domain(self):
        return self.__domain
