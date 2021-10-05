class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # dp solution
        # cur_winner: the winner idx of (i, k) i<=n
        cur_winner = 0
        for i in range(2, n+1):
            cur_winner = (cur_winner+k)%i
        return cur_winner+1
