from abc import ABC, abstractmethod
from solr.config import SOLR_BASE_URL
import requests
import json


class SolrCommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class CreateCoreCommand(SolrCommand):

    def __init__(self, core_name, instanceDir):
        self.core_name = core_name
        self.instanceDir = instanceDir

    def execute(self):
        response = requests.get(f"{SOLR_BASE_URL}/admin/cores?action=CREATE&name={self.core_name}&instanceDir={self.instanceDir}&configSet=solr-config")
        return response


class CreateItemInCoreCommand(SolrCommand):

    def __init__(self, core_name, item):
        self.core_name = core_name
        self.item = item

    def execute(self):
        headers = {
            "Content-type": "application/json"
        }
        data_json = json.dumps([self.item])
        response = requests.post(f"{SOLR_BASE_URL}/{self.core_name}/update?commit=true&overwrite=true", data=data_json, headers=headers)
        return response


class GetStatusCommand(SolrCommand):

    def __init__(self, core_name):
        self.core_name = core_name

    def execute(self):
        response = requests.get(f"{SOLR_BASE_URL}/admin/cores?action=STATUS")
        cores_status = response.json()["status"]
        if self.core_name in cores_status:
            return 200
        else:
            return 404


class ReloadCoreCommand(SolrCommand):

    def __init__(self, core_name):
        self.core_name = core_name

    def execute(self):
        response = requests.get(f"{SOLR_BASE_URL}/admin/cores?action=RELOAD&core={self.core_name}")
        return response
