import requests
import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class GetData(ABC):
    @abstractmethod
    def get_data(self, url):
        pass


class GetJson(GetData):
    def get_data(self, url):
        response = requests.get(url)
        data = json.loads(response.content)
        return data


class GetXml(GetData):
    def get_data(self, url):
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)
        data = {}
        for child in root:
            data[child.tag] = child.text

        return data


class JsonAdapter:
    def __init__(self, service):
        self.service = service

    def get_data(self, url):
        data = self.service.get_data(url)
        return json.dumps(data)


json_service = GetJson()
xml_service = GetXml()
json_data = json_service.get_data('https://jsonplaceholder.typicode.com/posts')
xml_data = xml_service.get_data('https://www.w3schools.com/xml/note.xml')

json_adapter = JsonAdapter(xml_service)

print(json_data)
print(xml_data)
print(type(json_adapter.get_data('https://www.w3schools.com/xml/note.xml')),json_adapter.get_data('https://www.w3schools.com/xml/note.xml'))
