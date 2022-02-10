class Node:
    def __init__(self):
        self.children = {}
        self.isword = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isword = True
    
    def query(self, suffix):
        cur = self.root
        ret = []
        for i,c in enumerate(suffix):
            
            if c in cur.children:
                cur = cur.children[c]
            else:
                break
            if cur.isword:
                return True
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        words = set(words)
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])
        self.q = deque([])

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        return self.trie.query(self.q)
