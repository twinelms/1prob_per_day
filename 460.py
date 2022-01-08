class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.pre = None
        self.next = None

class Lls:
    def __init__(self):
        self.dummy = self.tail = Node(0, 0)
        self.len = 0
    
    def remove(self, node):
        self.len -= 1
        pre, pos = node.pre, node.next
        pre.next = pos
        node.pre, node.next = None, None
        if node != self.tail:
            pos.pre = pre
        else:
            self.tail = pre
        
    def append(self, node):
        self.len += 1
        self.tail.next = node
        node.pre = self.tail
        self.tail = self.tail.next
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.f_lls = defaultdict(Lls)
        self.min_f = 0

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            self.f_lls[node.freq].remove(node)
            node.freq += 1
            self.f_lls[node.freq].append(node)
            if self.min_f == node.freq-1 and not self.f_lls[node.freq-1].len:
                self.min_f = node.freq
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.get(key)
            return
        if len(self.key_node) == self.cap:
                to_delete = self.f_lls[self.min_f].dummy.next
                self.f_lls[self.min_f].remove(to_delete)
                del self.key_node[to_delete.key]
        node = Node(key, value)
        self.key_node[key] = node
        self.f_lls[1].append(node)
        self.min_f = 1
