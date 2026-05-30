from heapbase import HeapBase


class MaxHeap(HeapBase):

    @staticmethod
    def should_swap(parent, child):

        return parent < child

    def insert(self, value):

        self.data.append(value)

        states = [{
            "before": self.data.copy(),
            "after": self.data.copy(),
            "operation":
            f"Insert {value}"
        }]

        i = len(self.data) - 1

        while i > 0:

            parent = (i - 1) // 2

            states.append({
                "before": self.data.copy(),
                "after": self.data.copy(),
                "comparing": [parent, i],
                "operation":
                f"Compare {self.data[parent]} with {self.data[i]}"
            })

            if self.should_swap(
                self.data[parent],
                self.data[i]
            ):

                before = self.data.copy()

                self.data[parent], self.data[i] = (
                    self.data[i],
                    self.data[parent]
                )

                states.append({
                    "before": before,
                    "after": self.data.copy(),
                    "swapping": [parent, i],
                    "operation":
                    f"Swap {before[parent]} and {before[i]}"
                })

                i = parent

            else:
                break

        return states

    def delete_index(self, index):

        if index < 0 or index >= len(self.data):

            return []

        states = []

        before = self.data.copy()

        self.data[index] = self.data[-1]

        self.data.pop()

        states.append({
            "before": before,
            "after": self.data.copy(),
            "swapping": [index],
            "operation":
            "Delete root"
        })

        if index < len(self.data):

            states.extend(
                self.heapify_down(index)
            )

        return states

    def heapify_down(self, i=0):

        states = []

        n = len(self.data)

        while True:

            left = 2 * i + 1

            right = 2 * i + 2

            target = i

            if left < n:

                states.append({
                    "before": self.data.copy(),
                    "after": self.data.copy(),
                    "comparing": [target, left],
                    "operation":
                    f"Compare {self.data[target]} with {self.data[left]}"
                })

                if self.should_swap(
                    self.data[target],
                    self.data[left]
                ):

                    target = left

            if right < n:

                states.append({
                    "before": self.data.copy(),
                    "after": self.data.copy(),
                    "comparing": [target, right],
                    "operation":
                    f"Compare {self.data[target]} with {self.data[right]}"
                })

                if self.should_swap(
                    self.data[target],
                    self.data[right]
                ):

                    target = right

            if target == i:
                break

            before = self.data.copy()

            self.data[i], self.data[target] = (
                self.data[target],
                self.data[i]
            )

            states.append({
                "before": before,
                "after": self.data.copy(),
                "swapping": [i, target],
                "operation":
                f"Swap {before[i]} and {before[target]}"
            })

            i = target

        return states