class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            string = "".join(sorted(x))
            if string in hashmap:
                hashmap[string].append(x)
            else:
                hashmap[string] = [x]
        return list(hashmap.values())