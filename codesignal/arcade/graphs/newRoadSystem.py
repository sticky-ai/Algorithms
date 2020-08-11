def newRoadSystem(roadRegister):
    check_1 = [i.count(True) for i in roadRegister]
    check_2 = [i.count(True) for i in zip(*roadRegister)]
    return check_1 == check_2
