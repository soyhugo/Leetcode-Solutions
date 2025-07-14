class Solution(object):
    def groupAnagrams(self, strs):

        anagram_groups = {}

        for word in strs:
            
            sorted_letters = "".join(sorted(word))

            if sorted_letters in anagram_groups:
                anagram_groups[sorted_letters].append(word)
            else:
                anagram_groups[sorted_letters] = [word]
                
        return anagram_groups.values()