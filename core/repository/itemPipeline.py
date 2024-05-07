from infra.solr.solrManager import SolrManager


class itemPipeline:

    def __init__(self):
        self.solr_manager = SolrManager()

    def save_item(self, item, core="v2"):
        response = self.solr_manager.add_item_to_core(core, item.__json__())
        return response.status_code
