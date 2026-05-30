def delete_heap(heap, index, should_swap):

    if index < 0 or index >= len(heap):
        return []

    states = []

    before = heap.copy()

    heap[index] = heap[-1]

    heap.pop()

    states.append({
        "before": before,
        "after": heap.copy(),
        "swapping": [index]
    })

    if index < len(heap):
        states.extend(
            heapify_down(heap, should_swap, index)
        )

    return states

def heapify_down(heap, should_swap, i=0):

    states = []

    n = len(heap)

    while True:

        left = 2 * i + 1
        right = 2 * i + 2

        target = i

        if left < n:

            states.append({
                "before": heap.copy(),
                "after": heap.copy(),
                "comparing": [target, left]
            })

            if should_swap(heap[target], heap[left]):
                target = left

        if right < n:

            states.append({
                "before": heap.copy(),
                "after": heap.copy(),
                "comparing": [target, right]
            })

            if should_swap(heap[target], heap[right]):
                target = right

        if target == i:
            break

        before = heap.copy()

        heap[i], heap[target] = heap[target], heap[i]

        states.append({
            "before": before,
            "after": heap.copy(),
            "swapping": [i, target]
        })

        i = target

    return states