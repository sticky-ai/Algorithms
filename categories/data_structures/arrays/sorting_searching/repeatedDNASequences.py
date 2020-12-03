from collections import Counter
def repeatedDNASequences(s):
    ds = Counter([s[i:i+10] for i in range(len(s) - 9)])
    return sorted([dna for dna, cnt in ds.items() if cnt > 1])
