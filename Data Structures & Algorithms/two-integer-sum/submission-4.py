class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in tracker:
                return [tracker[compliment], i]
            tracker[nums[i]] = i
        return []
