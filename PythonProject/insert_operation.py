def insert_heap(heap, value, should_swap):

    heap.append(value)

    states = [{
        "before": heap.copy(),
        "after": heap.copy()
    }]

    i = len(heap) - 1

    while i > 0:

        parent = (i - 1) // 2

        states.append({
            "before": heap.copy(),
            "after": heap.copy(),
            "comparing": [parent, i]
        })

        if should_swap(heap[parent], heap[i]):

            before = heap.copy()

            heap[parent], heap[i] = heap[i], heap[parent]

            states.append({
                "before": before,
                "after": heap.copy(),
                "swapping": [parent, i]
            })

            i = parent

        else:
            break

    return states