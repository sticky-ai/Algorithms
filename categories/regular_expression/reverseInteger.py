def reverseInteger(x):
    op = '+' if len(re.findall('\W', str(x))) == 0 else '-'
    num = re.findall('\d+', str(x))[0]
    return int(op + num[::-1])
