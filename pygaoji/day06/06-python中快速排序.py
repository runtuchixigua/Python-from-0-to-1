def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    pivot = list1[0]
    less = [i for i in list1[1:] if i <= pivot]
    greater = [i for i in list1[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    print(quick_sort(list1))
