def isPalindrome(st):
    return st == st[::-1]


def buildPalindrome(st):
    rvs = st[::-1]
    if isPalindrome(st) is True:
        return st
    
    for i in range(len(st)):
        if(isPalindrome(st + rvs[len(st) - i::])):
            return st + rvs[len(st) - i::]
    else:
        return st + rvs[1::]
