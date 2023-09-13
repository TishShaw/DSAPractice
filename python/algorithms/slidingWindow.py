# Leetcode 1838. Frequency of the most frequent element

def maxFrequency(nums, k):
    nums.sort()
    l, r, total, max_freq = 0, 0, 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1
        max_freq = max(max_freq, (r - l + 1))
        r += 1

    return max_freq


nums = [1, 2, 4]
k = 5
maxFrequency(nums, k)
