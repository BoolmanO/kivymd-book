from typing import Type


NameSpaceID = Type[str]


class Node:
    def __init__(self, data: dict[NameSpaceID, str]):
        self.data = data

    def req(self, id: NameSpaceID, text: str):
        self.data[id] = text

    def get(self, id: str):
        try:
            return self.data[id]
        except KeyError:
            return None


def create_node(data: dict[NameSpaceID, str]):
    return Node(data)


class TextManager:
    def __init__(self, nodes: dict[str, Node]):
        self.nodes = nodes

    def node(self, nodename: str):
        return self.nodes[nodename]