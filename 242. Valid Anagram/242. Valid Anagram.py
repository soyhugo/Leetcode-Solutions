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

        