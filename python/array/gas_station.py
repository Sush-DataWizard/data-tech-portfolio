# def canCompleteCircuit(gas, cost):
#     total_gas = 0      # Total gas available
#     total_cost = 0     # Total gas needed
#     tank = 0           # Current fuel in the tank
#     start_index = 0    # Current candidate starting station

#     for i in range(len(gas)):
#         total_gas += gas[i]
#         total_cost += cost[i]
#         tank += gas[i] - cost[i]

#         # If tank is negative, cannot reach station i+1 from current start
#         if tank < 0:
#             start_index = i + 1  # Try next station as starting point
#             tank = 0             # Reset tank

#     if total_gas < total_cost:
#         return -1

#     return start_index


def canCompleteCircuit(gas, cost):
        if sum(gas) < sum(cost):
            return -1
                
        curernt_gas = 0
        start = 0
        for i in range(len(gas)):
            curernt_gas += gas[i] - cost[i]
            if curernt_gas < 0:
                curernt_gas = 0
                start = i + 1

        return start



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]


# gas = [2,3,4]
# cost = [3,4,3]

print(canCompleteCircuit(gas, cost))