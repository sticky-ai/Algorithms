def isBalanced(s):
	d = {
		')' : '(',
		'}' : '{',
		']' : '['
	}

	stack = []

	for b in s:
		if stack:
			if d.get(b) == stack[-1]:
				stack.pop()
		else:
			stack.append(b)

	return 'NO' if stack else 'YES'

