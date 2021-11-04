import sys
"""
Generators
"""
def get_size_of_generated_list_and_standard_list(start: int, stop: int) -> tuple:
    lst = [num for num in range(start, stop)]
    g = (num for num in range(start, stop))
    return sys.getsizeof(lst), sys.getsizeof(g)

