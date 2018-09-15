class TopN:
    def __init__(self, size, sort_key=None, compare_func=None):
        self.size = size
        self.sort_key = sort_key
        self.compare_func = compare_func
        self.top = []

    def push(self, item):
        if len(self.top) < self.size:
            self.top.append(item)
            self.top.sort(key=self.sort_key, reverse=True)
        else:
            if self.compare_func is None:
                bln = self.top[self.size - 1] < item
            else:
                bln = self.compare_func(self.top[self.size - 1], item) < 0
            if bln:
                self.top[self.size - 1] = item
                self.top.sort(key=self.sort_key, reverse=True)


if __name__ == "__main__":
    topn = TopN(5, lambda item: item[0], lambda a, b: a[0] - b[0])
    for i in range(10):
        topn.push((i, 2, 3))
        print(topn.top)
