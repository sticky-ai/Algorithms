def solution(bridge_length, weight, truck_weights):
    on_bridge = [0] * bridge_length
    time = 0
    
    while on_bridge:
        time += 1
        on_bridge.pop(0)
        if len(truck_weights) != 0:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                on_bridge.append(0) 
        # print(time, on_bridge)
    return time
