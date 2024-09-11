def counting_sort(arr,exp):
    m = max(arr)
    counts = [0] * (m + 1)

    for i in arr:
        counts[i] += 1

    i = 0
    for c in range(m + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1


def radixsort(arr):
    max_ele = max(arr)
    exp = 1
    while max_ele // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = list(map(int, input("Enter the element with separated space: ").split()))
radixsort(arr)
for i in range(0, len(arr)):
    print(arr[i], end=' ')


