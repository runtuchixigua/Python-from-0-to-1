# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# s = "abcabcbb"
# s = "bbbbb"
# s = "aab"
s = "dvdf"


def lengthOfLongestSubstring(s):
    new_s = ''
    maxlen = 0
    for i in s:
        if i not in new_s:
            new_s += i
            maxlen = max(len(new_s), maxlen)
        else:
            new_s = new_s[new_s.index(i) + 1:]
            new_s += i
    return maxlen

print(lengthOfLongestSubstring(s))