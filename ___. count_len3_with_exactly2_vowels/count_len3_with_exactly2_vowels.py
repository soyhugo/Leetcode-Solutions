def count_len3_with_exactly2_vowels(word: str) -> int:
    vowels = set('aeiou')  # solo minúsculas
    n = len(word)
    if n < 3:
        return 0

    total = 0
    left, mid, right = 0, 1, 2
    while right < n:
        if ((word[left] in vowels and word[mid] in vowels and word[right] not in vowels) or
            (word[left] in vowels and word[mid] not in vowels and word[right] in vowels) or
            (word[left] not in vowels and word[mid] in vowels and word[right] in vowels)):
            total += 1

        left += 1
        mid  += 1
        right += 1

    return total
