def findEmailDomain(address):
    idx = address.rfind('@')
    return address[idx + 1:]

