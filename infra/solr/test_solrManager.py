import unittest
from infra.solr.solrManager import SolrManager
from core.entity.item import Item


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
    core_name = "test22"

    def check_core(self):
        status_code = self.solr_manager.get_core_status(self.core_name)
        if status_code != 200:
            response = self.solr_manager.create_core(self.core_name, "solr-config22")
            status_code = response.status_code
        return status_code

    def test_connection_to_solr(self):
        response = self.solr_manager.ping("v2")
        self.assertEqual(response.status_code, 200)

    def test_create_core(self):
        status_code = self.check_core()
        self.assertEqual(status_code, 200)

    def test_add_item_to_core(self):
        self.check_core()
        response = self.solr_manager.add_item_to_core(self.core_name, self.itemToTest.__json__())
        self.assertEqual(response.status_code, 200)

    def test_get_core_status(self):
        status_code = self.check_core()
        self.assertEqual(status_code, 200)

    def test_get_core_status_not_found(self):
        response = self.solr_manager.get_core_status("test51")
        self.assertEqual(response, 404)

    def test_reload_core(self):
        self.check_core()
        response = self.solr_manager.reload_core(self.core_name)
        self.assertEqual(response.status_code, 200)

    def test_reload_core_not_found(self):
        response = self.solr_manager.reload_core("test51")
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
