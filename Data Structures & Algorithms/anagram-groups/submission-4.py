class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            word = "".join(sorted(strs[i]))
            print(word)
            if word in hashmap:
                hashmap[word].append(x)
            else:
                hashmap[word] = x
            
        return list[hashmap]
        