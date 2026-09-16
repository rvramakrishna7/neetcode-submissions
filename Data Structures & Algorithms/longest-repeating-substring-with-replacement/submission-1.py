class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        left = 0
        max_length = 0
        max_freq = 0
        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_map[s[right]])

            window_length = right - left + 1

            while window_length - max_freq > k:
                freq_map[s[left]]-=1
                left+=1
                window_length = right - left + 1
            
            max_length = max(max_length, right - left + 1)
        return max_length