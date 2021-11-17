class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        most_freq_tasks = 0
        for t, f in count.items():
            if f == max_freq:
                most_freq_tasks += 1
        return max(len(tasks), (max_freq-1)*(n+1)+most_freq_tasks)
