class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = nums[0]
        for n in nums:
            if small > n:
                small = n
        return small




        