# 121 chars
return [f for e in [d.split('.')[-1] for d in eval(dir()[0])[0]] for f in ['commercial', 'organization', 'network', 'information'] if e in f]

# 160 chars 
# def domainType(domains):    
#     res = []
#     for e in [d.split('.')[-1] for d in domains]:
#         for f in ['commercial', 'organization', 'network', 'information']:
#             if e in f:
#                 res.append(f)
#     return res
