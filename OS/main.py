def fcfs(initial_head, requests):
    total_head_movements = abs(requests[0] - initial_head)
    for i in range(1, len(requests)):
        total_head_movements += abs(requests[i] - requests[i - 1])
    return total_head_movements

def scan(initial_head, requests):
    total_head_movements = 0
    direction = 1  # 1 for towards higher cylinder numbers, -1 for towards lower cylinder numbers
    index = 0
    while index < len(requests) and requests[index] < initial_head:
        index += 1
    if index > 0:  # if the initial head is not at the beginning
        total_head_movements += abs(requests[index - 1] - initial_head)
    while index < len(requests):
        total_head_movements += abs(requests[index] - requests[index - 1])
        index += 1
    total_head_movements += abs(requests[-1] - requests[index - 1])
    return total_head_movements

def c_scan(initial_head, requests):
    total_head_movements = 0
    index = 0
    while index < len(requests) and requests[index] < initial_head:
        index += 1
    if index > 0:  # if the initial head is not at the beginning
        total_head_movements += abs(requests[index - 1] - initial_head)
    if index < len(requests):  # if there are requests after initial head
        total_head_movements += abs(requests[-1] - requests[index])
    if index > 0:  # if there are requests before initial head
        total_head_movements += abs(requests[index - 1] - requests[0])
    return total_head_movements

def optimize_requests(requests, initial_head):
    # Reorder requests to minimize head movements
    # The basic idea is to sort the requests based on their proximity to the initial head position
    requests.sort(key=lambda x: abs(x - initial_head))
    return requests

def main():
    # Reading initial head position and requests from file
    with open("input.txt", "r") as file:
        initial_head = int(file.readline().strip())
        requests = [int(line.strip()) for line in file.readlines()]

    # Task 1: Original results
    print("Original results:")
    print("FCFS:", fcfs(initial_head, requests))
    print("SCAN:", scan(initial_head, requests))
    print("C-SCAN:", c_scan(initial_head, requests))

    # Sorting requests
    requests.sort()

    # Task 2: Optimized results
    print("\nOptimized results:")
    optimized_requests = optimize_requests(requests[:], initial_head)

    print("FCFS:", fcfs(initial_head, optimized_requests))  # FCFS remains unchanged

    # Optimizing SCAN
    optimized_requests_scan = optimize_requests(requests[:], initial_head)
    print("SCAN:", scan(initial_head, optimized_requests_scan))

    # Optimizing C-SCAN
    optimized_requests_c_scan = sorted(requests, key=lambda x: (initial_head - x) if x < initial_head else (x - initial_head))
    print("C-SCAN:", c_scan(initial_head, optimized_requests_c_scan))

if __name__ == "__main__":
    main()




