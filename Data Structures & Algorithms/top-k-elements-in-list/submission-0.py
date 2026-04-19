class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        result = []
        big = []
        while k > 0:
            big = max(hashmap, key=hashmap.get)
            result.append(big)
            del hashmap[big]
            k -= 1
        return result
