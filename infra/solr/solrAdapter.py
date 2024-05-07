from core.usecase.solrClient import SolrClient
from infra.solr.solrManager import SolrManager


class SolrManagerAdapter(SolrClient):
    def __init__(self):
        self.solr_manager = SolrManager()

    def add_item_to_core(self, core, item_json):
        return self.solr_manager.add_item_to_core(core, item_json)
