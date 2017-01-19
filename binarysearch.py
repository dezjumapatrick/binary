class BinarySearch(list):

    def __init__(self, c, d):
        super(BinarySearch, self).__init__(range(0, (c*d)+1, d)[1:])
        self.length = c

    def search(self, target):
        count = 0
        low = 0
        high = len(self) - 1
        if target > self[high] or target < self[low]:
            return dict([("count", count), ("index", -1)])
        while low <= high:
            midpoint = (low + high) // 2
            if self[high] == target:
                return dict([("count", count), ("index", high)])
            elif self[midpoint] > target:
                high = midpoint - 1
            elif self[midpoint] < target:
                low = midpoint + 1
            else:
                return dict([("count", count), ("index", midpoint)])
            if low == high:
                return dict([("count", count), ("index", -1)])
            count += 1