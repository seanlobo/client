from ..version.item import Item


class LineageEdge(Item):

    def __init__(self, json_payload):
        super(id, json_payload['tags'])
        self._name = json_payload['name']
        self._sourceKey = json_payload['sourceKey']

    # def __init__(id, other):
    #     super(id, other.get_tags())
    #     self._name = other._name
    #     self._sourceKey = other._sourceKey

    def get_name(self):
        return self._name

    def get_source_key(self):
        return self._sourceKey

    # NOTE: for get_tags(), even if lists contain same elements but different ordering, they are still not equal
    def __eq__(self, other):
        if not isinstance(other, RichVersion):
            return False
        return (self._name == other.name
            and self.get_id() == other.get_id()
            and self._sourceKey. == other.sourceKey
            and self.get_tags() == other.get_tags())