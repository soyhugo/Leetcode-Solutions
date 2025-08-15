class Solution:
  def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    freq_map = {}

    for char in s:
      if char in freq_map:
        freq_map[char] += 1
      else:
        freq_map[char] = 1
    for char in t:
      if char in freq_map:
        freq_map[char] -= 1
      else:
        freq_map[char] = 1

    for char in freq_map:
      if freq_map[char] != 0:
        return False
    return True
  
""""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1

        if freq_s == freq_t:
            return True
        else:
            return False

"""
        