def checkio(data):
    ret = []
    
    for item in data:
        # count returns the number of times x appears in the list, https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        if data.count(item) > 1:
            ret.append(item)
    return ret

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    assert list(checkio([1,2,3,4,1,2,3])) == [1,2,3,1,2,3], "My example"
    print("It is all good. Let's check it now")