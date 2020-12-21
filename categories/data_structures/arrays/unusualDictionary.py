def unusualDictionary(wordList):
    return wordList == sorted(wordList, key=lambda x: [x.split(' ')[-1], x.split(' ')[0]])
    
