from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        num, count = ctr.most_common(1)[0]
        return num