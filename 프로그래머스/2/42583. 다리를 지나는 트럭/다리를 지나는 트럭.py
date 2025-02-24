from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    waiting = deque(truck_weights)
    total_weight_on_bridge = 0
    
    while True:
        time += 1
        # 매 초마다 다리 위 트럭들의 남은 거리 -1
        # 만약 어떤 트럭의 남은 거리가 0이 되면 다리에서 제거
        for i in range(len(bridge)):
            bridge[i][1] -= 1
            
        if bridge and bridge[0][1] == 0:
            front_truck = bridge.popleft()
            total_weight_on_bridge -= front_truck[0]
            
        if waiting:
            if len(bridge) < bridge_length and (total_weight_on_bridge + waiting[0]) <= weight:
                truck = waiting.popleft()
                bridge.append([truck, bridge_length])
                total_weight_on_bridge += truck
                
        if not waiting and not bridge:
            return time