def select_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i+1 , len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j
        if min_index != i:
            list1[i], list1[min_index] = list1[min_index], list1[i]

if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9, 2, 4, 6, 1]
    select_sort(list1)
    print(list1)