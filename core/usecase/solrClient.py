from abc import ABC, abstractmethod


class SolrClient(ABC):
    @abstractmethod
    def add_item_to_core(self, core, item_json):
        pass
