import typing

# DO NOT MODIFY THIS CLASS
class Node:
    """ A graph node with a label and a list of neighbors. """

    def __init__(self,
            label: str,
            neighbors: typing.Union[typing.List["Node"], None] = None) -> None:
        self.label: str = label

        if (neighbors is None):
            neighbors = []

        self.neighbors: typing.List["Node"] = neighbors

    def __repr__(self) -> str:
        neighbor_labels = [neighbor.label for neighbor in self.neighbors]
        neighbors = ",".join(neighbor_labels)

        return f"Node(label = {self.label}, neighbors = [{neighbors}])"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented

        return self.label == other.label

    def __hash__(self) -> int:
        return hash(self.label)


# DO NOT MODIFY THIS CLASS
class Queue:
    """ A FIFO queue of (path, node) pairs. """

    nodes_expanded: int = 0

    def __init__(self) -> None:
        self._items: typing.List[typing.Tuple[typing.List[str], Node]] = []

    def __len__(self) -> int:
        """ Override the len() operator to get the size of the queue. """

        return len(self._items)

    def enqueue(self, item: typing.Tuple[typing.List[str], Node]) -> None:
        """ Enqueue the item into the queue. """

        self._items.insert(0, item)

    def dequeue(self) -> typing.Tuple[typing.List[str], Node]:
        """ Dequeue the earliest enqueued item still in the queue. """

        Queue.nodes_expanded += 1
        return self._items.pop()

    def is_empty(self) -> bool:
        """ Returns True if the queue is empty. """

        return len(self._items) == 0


# TODO(participant): Debugg the code bellow.
def breadth_first_search(start_node: Node, goal_node: Node) -> typing.List[str]:
    raise NotImplementedError
