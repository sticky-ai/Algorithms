ars
q = re.sub(' +', ' ', eval(dir()[0])[0].strip())
q = list(re.sub('\?+', '?', re.sub('\s?,\s?', ', ', q)))

if q[-1] != '?':
        q += '?'

	q[0] = q[0].upper()
	return ''.join(q)

# 152 chars
# q = re.sub(' +', ' ', eval(dir()[0])[0].strip())
# q = re.sub('\s?,\s?', ', ', q)
# q = re.sub('\?+', '?', q)

# q = list(q)
# if q[-1] != '?':
#     q += '?'

# q[0] = q[0].upper()
# return ''.join(q)

# OG (182 chars)
# def questionCorrectionBot(question):
#     q = re.sub(' +', ' ', question.strip())
#     q = re.sub('\s?,\s?', ', ', q)
#     q = re.sub('\?+', '?', q)
    
#     if list(q)[-1] != '?':
#         q += '?'

#     q = list(q)
#     q[0] = q[0].upper()
#     return ''.join(q)
