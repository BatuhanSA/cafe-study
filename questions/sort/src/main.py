#!/usr/bin/env python3
import typing

# ONLY MODIFY THE SECTIONS MARKED WITH "TODO" IN THIS CLASS
class TrackedList:
    """ A list that counts comparisons while sorting. """

    def __init__(self, data: typing.List[int]) -> None:
        """ Store the data to be sorted. """

        self.data: typing.List[int] = data
        self.num_comps: int = 0

    def comp(self, a: int, b: int) -> bool:
        """ Return True if a > b, and count the comparison. """

        self.num_comps += 1
        return a > b

    def get_list(self) -> typing.List[int]:
        """ Return the list. """

        return self.data

    def get_num_comps(self) -> int:
        """ Return the number of comparisons made. """

        return self.num_comps

    # TODO(participant): Debugg the code bellow.
    def bubble_sort(self) -> None:

        for _ in range(len(self.data)):
            for i in range(len(self.data) - 1):
                j = i + 1
                if (self.comp(self.data[i], self.data[j])):
                    aux = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = aux
        return
