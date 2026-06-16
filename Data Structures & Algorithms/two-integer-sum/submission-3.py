class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in myHashMap:
                return [myHashMap[complement], i]
            myHashMap[num] = i