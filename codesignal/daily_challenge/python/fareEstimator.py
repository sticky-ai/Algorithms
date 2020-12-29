# 51 chars
A, B, *C = eval(dir()[0])
return [A * t + B * d for t, d in zip(*C)]

# 54 chars
# A, B, C, D = eval(dir()[0])
# return [A * t + B * d for t, d in zip(C, D)]

# Original
# def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
#     return [ride_time * t + ride_distance * d for t, d in zip(cost_per_minute, cost_per_mile)]
        
