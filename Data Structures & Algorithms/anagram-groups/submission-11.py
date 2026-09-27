class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        count_dict = {}

        for string in strs:
            count = [0] * 26

            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            final_count = tuple(count)

            if final_count in count_dict:
                count_dict[final_count].append(string)
            else:
                count_dict[final_count] = [string]
        
        return list(count_dict.values())
                