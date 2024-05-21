

class itemPipeline:

    def __init__(self, solrClientManager):
        self.solr_manager = solrClientManager

    def save_item(self, item, core="v2"):
        response = self.solr_manager.add_item_to_core(core, item.__json__())
        return response.status_code
