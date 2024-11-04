import json
from xml.etree import ElementTree


class BaseSerializeBook:
    SERIALIZE_METHODS = []

    def json_serialize(self) -> json.dumps:
        return json.dumps({"title": self.title, "content": self.content})

    def xml_serialize(self) -> ElementTree.tostring:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")

    def action_serialize(self):
        pass

    def serialize(self, serialize_type: str) -> str:
        if serialize_type not in self.SERIALIZE_METHODS:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        self.action_serialize()


class XmlSerializeBook(BaseSerializeBook):
    SERIALIZE_METHODS = super().SERIALIZE_METHODS + ["xml"]

    def action_serialize(self) -> ElementTree.tostring:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")


class JsonSerializeBook(BaseSerializeBook):
    SERIALIZE_METHODS = super().SERIALIZE_METHODS + ["json"]

    def action_serialize(self) -> json.dumps:
        return json.dumps({"title": self.title, "content": self.content})
