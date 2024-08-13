'''
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''


def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target and i != j:
    #             return [i, j]
    # i = 0

    # -----------------------
    # while i < len(nums):
    #     j = i + 1
    #     while j < len(nums):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    #         j = j + 1
    #     i = i + 1
    # ---------------------------
    # for i in range(len(nums)):
    #     a = target - nums[i]
    #     if a in nums[i + 1:]:
    #         return [i, nums[i + 1:].index(a) + i + 1]
    #---------------------------------
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []



nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums1 = [3, 3]
target2 = 6
print(twoSum(nums1, target2))




