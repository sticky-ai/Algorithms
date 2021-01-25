def simplifyPath(path):
    stack = []
    path = [p for p in path.split('/') if p != ''][::-1]
    
    while path:
        p = path.pop()
        if p == '..':
            if stack:
                stack.pop()
            else:
                continue
        elif p == '.':
            continue
        else:
            stack.append(p)

    return '/' + '/'.join(stack)
