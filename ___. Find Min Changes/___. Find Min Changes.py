# ------------------------------------------------------------
# Problem: Palindromic Periodic Password
#
# Description:
# Given a lowercase string `currentPassword` and an integer `k`,
# convert it to a new string of the same length that:
#   1. Is a palindrome
#   2. Has period `k` (i.e. s[i] == s[i + k] for all valid i)
# The goal is to minimize the number of character changes.
#
# Function Signature:
# def findMinChanges(currentPassword: str, k: int) -> int
#
# Constraints:
# - 1 <= k <= len(currentPassword) <= 2 * 10^5
# - len(currentPassword) is divisible by k
#
# Examples:
# Input:  currentPassword = "abzzbz", k = 3
# Output: 1
#
# Input:  currentPassword = "vsvsvv", k = 3
# Output: 0
#
# Tags: Strings, Palindrome, Periodicity, Greedy
# ------------------------------------------------------------

def findMinChanges(s, k):
    n = len(s)
    visited = [False] * n
    changes = 0

    for i in range(n):
        if visited[i]:
            continue

        group = set()
        stack = [i]

        while stack:
            idx = stack.pop()
            if idx in group:
                continue
            group.add(idx)

            mirror = n - 1 - idx
            period = (idx + k) % n
            stack.extend([mirror, period])

        freq = [0] * 26
        for idx in group:
            visited[idx] = True
            freq[ord(s[idx]) - ord('a')] += 1

        max_freq = max(freq)
        changes += len(group) - max_freq

    return changes
