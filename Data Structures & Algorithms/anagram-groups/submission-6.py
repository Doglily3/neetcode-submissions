class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            word = "".join(sorted(x))
            if word in hashmap:
                hashmap[word].append(x)
            else:
                hashmap[word] = [x]
            
        return list(hashmap.values())
        