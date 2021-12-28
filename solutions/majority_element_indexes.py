from collections import Counter
"""
Return a list of the indexes of the majority element.
The majority element is the element that appears more than floor(n/2) times.
If there is no majority element, return an empty list.
"""


def majority_element_indexes(elements: [int]) -> [int]:
    if not elements:
        return []

    count = Counter(elements)
    majority_el = list(count.keys())[0]

    return [
        i for i, elem in enumerate(elements) if elem == majority_el
    ] if count[majority_el] > len(elements)//2 else []


print(majority_element_indexes([]))
print(majority_element_indexes([4, 4, 1, 4, 1, 4, 1, 4]))
