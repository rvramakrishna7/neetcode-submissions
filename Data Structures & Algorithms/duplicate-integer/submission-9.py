
class Solution:
    def hasDuplicate(self, nums :  List[int])-> bool:
        tracker = set()
        n = len(nums)
        for i in range(n):
            if nums[i] not in tracker:
                tracker.add(nums[i])
            else:
                return True
        return False
