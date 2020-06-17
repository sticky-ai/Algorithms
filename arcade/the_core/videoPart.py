from math import gcd

def videoPart(part, total):
    part_time = map(int, part.split(':'))
    total_time = map(int, total.split(':'))
    
    t = 3600
    part_sum = 0
    for time in part_time:
        part_sum += t * time
        t /= 60
    
    t = 3600
    total_sum = 0
    for time in total_time:
        total_sum += t * time
        t /= 60
    
    gcd_num = gcd(int(part_sum), int(total_sum))
    return [int(part_sum) / gcd_num, int(total_sum) / gcd_num]
