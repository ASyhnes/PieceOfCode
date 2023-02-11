#trie valeur maximum 'une liste

from typing import List

 
def highest(numbers: List[int]) -> int:
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value