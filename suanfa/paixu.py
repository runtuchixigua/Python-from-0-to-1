arr = [64, 34, 25, 12, 22, 11, 90]


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# print(bubbleSort(arr))

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [l for l in arr[1:] if pivot > l]
        right = [r for r in arr[1:] if pivot <= r]
        return quickSort(left) + [pivot] + quickSort(right)


# print(quickSort(arr))


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort(arr))


