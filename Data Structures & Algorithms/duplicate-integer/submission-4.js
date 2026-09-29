class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const tracker = new Set();
        for (const num of nums) {
            if(tracker.has(num)) return true;
            tracker.add(num)
        }
        return false;
    }
}
