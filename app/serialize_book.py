import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class BaseSerializeBook(ABC):

    @abstractmethod
    def serialize(self, method_type: str) -> None:
        pass


class XmlSerializeBook(BaseSerializeBook):

    def serialize(self, method_type: str) -> ElementTree.tostring:
        if method_type == "xml":
            root = ElementTree.Element("book")
            title = ElementTree.SubElement(root, "title")
            title.text = self.title
            content = ElementTree.SubElement(root, "content")
            content.text = self.content
            return ElementTree.tostring(root, encoding="unicode")

        else:
            super().serialize(method_type)


class JsonSerializeBook(BaseSerializeBook):

    def serialize(self, method_type: str) -> str:
        if method_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        else:
            super().serialize(method_type)


class SerializeBook(JsonSerializeBook, XmlSerializeBook):
    pass
