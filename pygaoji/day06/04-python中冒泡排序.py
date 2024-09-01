def bubble_sort(list1):
    for i in range(len(list1) - 1):
        flag = False
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                flag = True
        if not flag:
            break



if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 1]
    # list2 = [1,2,3,4,5]
    bubble_sort(list1)
    # bubble_sort(list2)
    print(list1)
    # print(list2)


