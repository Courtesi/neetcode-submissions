class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        count_dict = {}

        for string in strs:
            count = [0] * 26

            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            x = list(map(str, count))
            hash_string = ",".join(x)

            if hash_string in count_dict:
                count_dict[hash_string].append(string)
            else:
                count_dict[hash_string] = [string]
        
        return list(count_dict.values())
                