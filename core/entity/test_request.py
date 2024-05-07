import unittest
from core.entity.request import Request


class TestRequest(unittest.TestCase):
    def test_extract_domain_http(self):
        url_http = "http://example.com/path"
        request_http = Request(url_http)
        self.assertEqual(request_http.domain, "example.com")

    def test_extract_domain_https(self):
        url_https = "https://www.example.com/path"
        request_https = Request(url_https)
        self.assertEqual(request_https.domain, "www.example.com")

    def test_extract_domain_custom_port(self):
        url_port = "http://example.com:8080/path"
        request_port = Request(url_port)
        self.assertEqual(request_port.domain, "example.com:8080")

    def test_extract_domain_subdomain(self):
        url_subdomain = "http://sub.example.com/path"
        request_subdomain = Request(url_subdomain)
        self.assertEqual(request_subdomain.domain, "sub.example.com")

    def test_extract_domain_no_scheme(self):
        url_no_scheme = "example.com/path"
        request_no_scheme = Request(url_no_scheme)
        self.assertNotEqual(request_no_scheme.domain, "example.com")


if __name__ == '__main__':
    unittest.main()
