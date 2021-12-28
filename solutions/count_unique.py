"""
Count unique chars without using a set
"""
def count_unique(chars: str) -> int:
    seen_c = []
    chars = chars.strip() # O(n)
    for char in chars:  # O(n)
        if char not in seen_c:  # O(n)
            seen_c.append(char)  # O(1)
    return len(seen_c)


"""
Count unique chars using a set
"""
def count_unique_with_set(chars: str) -> int:
    # return len({c for c in chars})  # same as method below
    return len(set(chars))

