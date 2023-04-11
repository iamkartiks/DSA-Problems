def can_complete_circuit(gas, cost):
    n = len(gas)
    total_gas = total_cost = tank = start = 0
    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total_gas >= total_cost else -1
