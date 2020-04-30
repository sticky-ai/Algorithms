def transposeDictionary(scriptByExtension):
    return sorted([i for i in zip(scriptByExtension.values(), scriptByExtension.keys())])

