import json
from xml.etree import ElementTree


class SerializeBook:
    SERIALIZE_METHODS = ["json", "xml"]

    def json_serialize(self) -> json.dumps:
        return json.dumps({"title": self.title, "content": self.content})

    def xml_serialize(self) -> ElementTree.tostring:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")

    def serialize(self, serialize_type: str) -> str:
        if serialize_type not in self.SERIALIZE_METHODS:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        match serialize_type:
            case "json":
                return self.json_serialize()

            case "xml":
                return self.xml_serialize()
