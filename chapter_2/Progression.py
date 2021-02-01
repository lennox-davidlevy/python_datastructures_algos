class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            result = self._current
            self._advance()
            return result

    def __iter__(self, n):
        return self

    def print_progressions(self, n):
        print(" ".join(str(next(self)) for j in range(n)))
