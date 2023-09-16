import heapq

def merge_lists(k_lists):
    k = len(k_lists)
    heap = []
    sorted_list = []

    for i in range(k):
        if k_lists[i] is not None and k_lists[i][-1] is not None:
            heapq.heappush(heap, (k_lists[i].pop(0), i))
    
    while heap:
        current = heapq.heappop(heap)
        data = current[0]
        i = current[1]
        sorted_list.append(data)
        if len(k_lists[i]) > 0:
            heapq.heappush(heap, (k_lists[i].pop(0), i))

    return sorted_list


if __name__ == "__main__":
    ls = [[1, 2, 3, 4], [-1, 3, 56], [12, 15, 18]]

    print(merge_lists(ls));