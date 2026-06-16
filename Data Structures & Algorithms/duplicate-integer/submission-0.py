class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = nums.copy()
        length = len(nums)
        for i in range(length):
            num = nums[i]
            for j in range(length):
                num2 = nums[j]
                if ((num2 == num) and (i != j)):
                    return True

        return False
