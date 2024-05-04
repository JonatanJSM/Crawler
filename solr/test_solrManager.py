import unittest
from solr.solrManager import SolrManager
from crawler.item import Item


class TestSolrUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.solr_manager = SolrManager()

    itemToTest = Item(
        "Este es el título de la página",
        "meta titulo",
        "html",
        "Este es la descripción de la página",
        "https://wagslane.com/",
        "Blog")

    def test_connection_to_solr(self):
        response = self.solr_manager.ping("v2")
        self.assertEqual(response.status_code, 200)

    def test_create_core(self):
        response = self.solr_manager.create_core("test22", "solr-config22")
        self.assertEqual(response.status_code, 200)

    def test_add_item_to_core(self):
        response = self.solr_manager.add_item_to_core("test50", self.itemToTest.__json__())
        self.assertEqual(response.status_code, 200)

    def test_get_core_status(self):
        response = self.solr_manager.get_core_status("test50")
        self.assertEqual(response, 200)

    def test_get_core_status_not_found(self):
        response = self.solr_manager.get_core_status("test51")
        self.assertEqual(response, 404)

    def test_reload_core(self):
        response = self.solr_manager.reload_core("test50")
        self.assertEqual(response.status_code, 200)

    def test_reload_core_not_found(self):
        response = self.solr_manager.reload_core("test51")
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
