class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1
        for right in range(len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1

            if right >= len(s1):
                left_char = s2[right - len(s1)]
                s2_count[left_char] -= 1
                if s2_count[left_char] == 0:
                    del s2_count[left_char]
            if s1_count == s2_count:
                return True
        return False
