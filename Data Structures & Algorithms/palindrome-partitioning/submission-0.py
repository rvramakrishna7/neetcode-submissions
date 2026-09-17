class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_Palindrome(sub_string: str) -> bool:
            return sub_string == sub_string[::-1]

        def backtrack(start: int):
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]

                if is_Palindrome(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
