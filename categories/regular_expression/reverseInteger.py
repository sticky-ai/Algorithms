def reverseInteger(x):
    op = re.findall('\W', str(x))
    nums = re.findall('[0-9]+', str(x))[0]
    return int(nums[::-1]) if len(op) == 0 else int(op[0] + str(nums[::-1]))
