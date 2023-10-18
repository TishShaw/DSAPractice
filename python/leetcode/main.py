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
