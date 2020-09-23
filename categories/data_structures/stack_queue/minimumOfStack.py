def minimumOnStack(operations):
    stack = []
    whole = []
    for op in operations:
        if op == 'min':
            whole.append(min(map(int, stack)))
        elif op == 'pop':
            stack.pop()
        else:
            o, v = op.split(' ')
            stack.append(v)

    return whole
