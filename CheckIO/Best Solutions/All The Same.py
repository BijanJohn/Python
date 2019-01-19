from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return elements[1:] == elements[:-1]

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    assert all_the_same([3,4,5]) == False
    print("This is Dope Shit!")