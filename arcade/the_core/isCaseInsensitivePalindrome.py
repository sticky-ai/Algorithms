def isCaseInsensitivePalindrome(inputString):
    return inputString.lower() == inputString.lower()[::-1]
