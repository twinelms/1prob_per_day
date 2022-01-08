class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isword = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isword = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        res = []
        
        def search(i, j, cur, path):
            if cur.isword:
                res.append(path)
                cur.isword = False
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '.':
                return
            c = board[i][j]
            if c not in cur.children:
                return
            board[i][j] = '.'
            search(i-1, j, cur.children[c], path+c)
            search(i+1, j, cur.children[c], path+c)
            search(i, j-1, cur.children[c], path+c)
            search(i, j+1, cur.children[c], path+c)
            board[i][j] = c
            if not cur.children[c].children:
                del cur.children[c]
            
        for i in range(m):
            for j in range(n):
                search(i, j, trie.root, '')
        return res
