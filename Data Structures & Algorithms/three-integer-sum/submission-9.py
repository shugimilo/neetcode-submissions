from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numSet = set(nums)
        used = set()
        numCounter = Counter(nums)
        res = []
        if numCounter[0] >= 3:
            res.append([0, 0, 0])
        i = 0
        j = len(nums)-1
        for i in range(0, len(nums)):
            used.add(i)
            for j in range(0, len(nums)):
                if j not in used:
                    iNum, jNum, kNum = nums[i], nums[j], -(nums[i]+nums[j])
                    if kNum in numSet and kNum != iNum and kNum != jNum:
                        print(f"iNum = {iNum}, jNum = {jNum}, kNum = {kNum}")
                        triplet = sorted([iNum, jNum, kNum])
                        if triplet not in res:
                            res.append(triplet)

        return res