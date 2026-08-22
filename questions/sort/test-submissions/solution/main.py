#!/usr/bin/env python3

# ONLY MODIFY THE SECTIONS MARKED WITH "TODO" IN THIS CLASS
class TrackedList:
    def __init__(self, data):
        self.data = data
        self.num_comps = 0

    def comp(self, a, b):
        self.num_comps += 1
        return a > b

    def get_list(self):
        return self.data

    def get_num_comps(self):
        return self.num_comps

    # TODO(participant): Debugg the code bellow.
    def bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.data) - 1):
                j = i + 1
                if (self.comp(self.data[i], self.data[j])):
                    swapped = True
                    aux = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = aux
        return
