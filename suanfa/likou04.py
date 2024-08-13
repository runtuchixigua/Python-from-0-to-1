def findMedianSortedArrays(nums1, nums2):
    nums1 = nums1 + nums2
    nums1.sort()
    if len(nums1) % 2 == 0:
        return (nums1[int(len(nums1) / 2)] + nums1[int(len(nums1) / 2) - 1]) / 2
    else:
        return nums1[int(len(nums1) / 2)]


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))


