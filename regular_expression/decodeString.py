"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be
decodeString(s) = "abababab";

For s = "2[b3[a]]", the output should be
decodeString(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
decodeString(s) = "zyzzzabcabc".
"""

def decodeString(s):
    p = re.compile('(\d+)\[(\w+)\]')
    s = re.sub(p, r' \2*\1 ', s).split(' ')
    s = [v for v in s if v != '']

    res = ''
    for v in s:
        if '*' in v:
            temp = v.split('*')
            res += temp[0] * int(temp[1])
        else:
            res += v
    
    if '[' in res:
        return decodeString(res)
    else:
        return res
