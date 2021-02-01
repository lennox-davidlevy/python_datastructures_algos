class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Step cannot be 0")
        if stop == None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k = k + len(self)
        if not 0 <= k < self._length:
            raise IndexError(f"index({k} is out of range)")

        return self._start + (k * self._step)


r = Range(12)
for i in r:
    print(i)
