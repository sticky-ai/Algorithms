import re

def solution(s):
    print(re.findall('\{[0-9]+.*?\}', s[1:-1]))
	# {1, 2, 3}, {1}, {2, 3} ==> '{1, 2, 3}', '{1}', '{2, 3}'
