class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq_buckets = [[] for i in range(len(nums))]

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        for num, cnt in count.items():
            freq_buckets[cnt - 1].append(num)

        res = []

        for i in range(len(freq_buckets) - 1, -1, -1):
            if freq_buckets[i]:
                for j in freq_buckets[i]:
                    if k > 0:
                        res.append(j)
                        k -= 1
                    else:
                        return res
        
        return res