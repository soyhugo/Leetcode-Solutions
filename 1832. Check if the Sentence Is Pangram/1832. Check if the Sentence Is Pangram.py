class Solution:
  def checkIfPangram(self, sentence):
    letters_seen = set()
    for char in sentence:
      if char.isalnum():
        letters_seen.add(char.lower())
    if len(letters_seen) == 26:
      return True
    return False
