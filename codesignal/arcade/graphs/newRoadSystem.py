def newRoadSystem(roadRegister):
    check_1 = [i.count(True) for i in roadRegister]
    check_2 = [i.count(True) for i in zip(*roadRegister)]
    return check_1 == check_2

# def newRoadSystem(roadRegister):
#     d = dict()
    
#     for i in range(len(roadRegister)):
#         d[i] = [0, 0]
    
#     for i in range(len(roadRegister)):
#         for j in range(len(roadRegister)):
#             if i != j and roadRegister[i][j]:
#                 d[i][0] += 1
#                 d[j][1] += 1
    
#     return all([r == c for r, c in d.values()])
