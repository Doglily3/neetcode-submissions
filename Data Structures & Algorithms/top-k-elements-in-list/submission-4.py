class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        result = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in result[:k]]