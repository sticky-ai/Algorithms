def isInformationConsistent(evidences):
    evidence = [e for e in zip(*evidences)]
    for e in evidence:
        temp = [num for num in e if num != 0]
        if len(set(temp)) >= 2:
            return False
    return True
