class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(numbers):
            for j, num2 in enumerate(numbers):
                if num1 + num2 == target and i != j:
                    return [i+1, j+1]
