from infra.gateway.solr.solrManagerMeta import SolrManagerMeta
from infra.gateway.solr.solrCommands import (
    CreateCoreCommand, CreateItemInCoreCommand,
    GetStatusCommand, ReloadCoreCommand
    )
from infra.gateway.solr.config import SOLR_BASE_URL
import requests


class SolrManager(metaclass=SolrManagerMeta):

    def __init__(self):
        pass

    def ping(self, core_name=None):
        if core_name:
            url = f"{SOLR_BASE_URL}/{core_name}/admin/ping"
        else:
            url = f"{SOLR_BASE_URL}/admin/ping"
        response = requests.get(url)
        return response

    def create_core(self, core_name, instanceDir):
        create_core_command = CreateCoreCommand(core_name, instanceDir)
        response = create_core_command.execute()
        return response

    def add_item_to_core(self, core_name, item):
        create_item_in_core_command = CreateItemInCoreCommand(core_name, item)
        response = create_item_in_core_command.execute()
        return response

    def get_core_status(self, core_name):
        get_status_command = GetStatusCommand(core_name)
        response = get_status_command.execute()
        return response

    def reload_core(self, core_name):
        reload_core_command = ReloadCoreCommand(core_name)
        response = reload_core_command.execute()
        return response
