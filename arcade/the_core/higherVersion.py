def higherVersion(ver1, ver2):
    v1, v2 = map(int, ver1.split('.')), map(int, ver2.split('.'))
    return list(v1) > list(v2)
