from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        num, _ = ctr.most_common(1)[0]
        return num