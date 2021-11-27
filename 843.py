class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def compare(w1, w2):
            ret = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    ret += 1
            return ret
        
        for i in range(10):
            guess = random.choice(wordlist)
            match = master.guess(guess)
            new = []
            for w in wordlist:
                if compare(w, guess) == match:
                    new.append(w)
            wordlist = new
