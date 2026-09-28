class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            complement  = target - nums[i]
            if complement in tracker:
                return [tracker[complement],i]
            tracker[nums[i]] = i
        return []