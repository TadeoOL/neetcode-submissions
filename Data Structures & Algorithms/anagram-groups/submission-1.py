class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_table = {}
        result = []
        for i in strs:
            word = i.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in hash_table:
                hash_table[sorted_word].append(word)
            else:
                hash_table[sorted_word] = [word]
        for i in hash_table:
            result.append(hash_table[i])
        return result