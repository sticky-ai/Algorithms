def removeDuplicateCharacters(str):
    return ''.join([s for s in str if str.count(s) < 2])


#def removeDuplicateCharacters(str):
#    e = [s for s in set(str) if str.count(s) > 1]
#    return ''.join([s for s in str if s not in e])
