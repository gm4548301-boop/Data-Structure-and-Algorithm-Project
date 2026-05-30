class HeapBase:

    def __init__(self):

        self.data = []

    def snapshot(self):

        return {
            "before": self.data.copy(),
            "after": self.data.copy()
        }