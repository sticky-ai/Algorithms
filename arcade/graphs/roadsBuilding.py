from itertools import combinations

def roadsBuilding(cities, roads):
    ways = [list(i) for i in combinations(range(cities), 2)]
    new_roads = [i for i in ways if i not in roads]
    return [i for i in new_roads if list(reversed(i)) not in roads]
    
