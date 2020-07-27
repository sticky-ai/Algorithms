def groupsOfAnagrams(words):
    return len(set([''.join(sorted(w)) for w in words]))
