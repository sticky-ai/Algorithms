def splitAddress(address):
    return [add for add in re.findall('\w+', address) if add != 'com']
