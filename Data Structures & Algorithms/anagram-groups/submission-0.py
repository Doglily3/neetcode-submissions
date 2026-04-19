class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringSorted = []
        for x in strs:
            stringSorted.append("".join(sorted(x)))
        hashmap={}
        for i, x in enumerate(stringSorted):
            if x in hashmap:
                hashmap[x].append(strs[i])
            else:
                hashmap[x]= [strs[i]]
        return list(hashmap.values())

