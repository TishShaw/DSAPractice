# Leetcode 1768. Merge Strings Alternately
def mergeAlternately(self, word1: str, word2: str) -> str:
    i, j = 0, 0
    result = []

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)


# Leetcode 1822. Sign of the Product of an Array
def arraySign(self, nums: List[int]) -> int:
    neg = 0

    for n in nums:
        if n == 0:
            return 0
        neg += (1 if n < 0 else 0)

    return -1 if neg % 2 else 1


#  1071. Greatest Common Divisor of Strings
def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    len1, len2 = len(str1), len(str2)

    common_len = gcd(len1, len2)

    common_substring = str1[:common_len]

    if str1 == common_substring * (len1 // common_len) and str2 == common_substring * (len2 // common_len):
        return common_substring
    else:
        return ""


# 345. Reverse Vowels of a String
def reverseVowels(self, s: str) -> str:
    chars = list(s)
    kVowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and chars[l] not in kVowels:
            l += 1
        while l < r and chars[r] not in kVowels:
            r -= 1

        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1

    return "".join(chars)


# 151. Reverse Words in a String
def reverseWords(self, s: str) -> str:
    newStr = s.split()
    l, r = 0, len(newStr) - 1

    while l <= r:
        temp = newStr[l]
        newStr[l] = newStr[r]
        newStr[r] = temp

        l += 1
        r -= 1

    return " ".join(newStr)


# 238. Product of Array Except Self
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n

    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    suffix = 1
    for i, num in reversed(list(enumerate(nums))):
        ans[i] *= suffix
        suffix *= num

    return ans
