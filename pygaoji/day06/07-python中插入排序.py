def insert_sort(list1):
    for i in range(1, len(list1)):
        for j in range(i, 0, -1):
            if list1[j] < list1[j - 1]:
                list1[j], list1[j - 1] = list1[j - 1], list1[j]



if __name__ == '__main__':
    list1 = [1, 5, 3, 7, 9, 2, 4, 6, 8]
    insert_sort(list1)
    print(list1)