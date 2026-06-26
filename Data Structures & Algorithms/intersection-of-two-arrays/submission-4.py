class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            shorter, longer = set(nums1), set(nums2)
        else:
            shorter, longer = set(nums2), set(nums1)
        
        intersection = []

        for num in shorter:
            if num in longer:
                intersection.append(num)

        return intersection