def uniqueCharacters(document):
    return list(map(chr, sorted(list(map(ord, set(document))))))

