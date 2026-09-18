class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w
        
        ROWS,COLS = len(board), len (board[0])
        res = []

        def dfs(r,c,node):
            char  = board[r][c]

            if char not in node.children:
                return
            curr_node = node.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = '#'

            directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in directions:
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr,nc,curr_node)
            board[r][c] = char
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return res
        