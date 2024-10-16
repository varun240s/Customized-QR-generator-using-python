from collections import deque

def findMin(arr):
    n = len(arr)
    unique_values = set(arr)
    min_time = float('inf')
    
    for value in unique_values:
        time = bfs_min_time(arr, value)
        min_time = min(min_time, time)
    
    return min_time

def bfs_min_time(arr, value):
    n = len(arr)
    visited = [False] * n
    queue = deque()
    
    # Initialize the BFS with all positions having the chosen value
    for i in range(n):
        if arr[i] == value:
            queue.append((i, 0))  # (index, time)
            visited[i] = True
    
    max_time = 0
    
    while queue:
        current_index, current_time = queue.popleft()
        max_time = max(max_time, current_time)
        
        # Check adjacent positions
        for next_index in (current_index - 1, current_index + 1):
            if 0 <= next_index < n and not visited[next_index]:
                queue.append((next_index, current_time + 1))
                visited[next_index] = True
    
    return max_time

if __name__ == "__main__":
    arr_count = int(input().strip())
    arr = []
    
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    
    result = findMin(arr)
    print(result)
