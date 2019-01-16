def checkio(data):
    ret = []
    
    for item in data:
        if data.count(item) > 1:
            ret.append(item)
    return ret

numbers = [1,2,3,2,1]
print checkio(numbers)