from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        return ValueError("value not in sequence")

    def count(self, val):
        count = 0
        for j in range(len(self)):
            if self[j] == val:
                count += 1
        return count
