class RandomizedSet:

    def __init__(self):
        self.ele={}
        self.arr=[]

    def insert(self, val: int) -> bool:
        if val in self.ele: return False
        i=len(self.arr)
        self.ele[val]=i
        self.arr.append(val)
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.ele: return False
        i=self.ele[val]
        self.arr[i]=self.arr[-1]
        self.ele[self.arr[i]]=i
        self.arr.pop()
        del self.ele[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)
