import sys
import random

# read file and convert each line to an integer representing a cylinder request
def read_requests(file_name):
    with open(file_name, 'r') as file:
        return [int(line.strip()) for line in file]

# FCFS algorithm implementation
def fcfs(requests, initial_position):
    head_movements = 0  
    current_position = initial_position  
    # service requests in the order they arrive
    for request in requests:
        head_movements += abs(request - current_position)  # add distance to the next request
        current_position = request 
    return head_movements 

# SCAN algorithm implementation
def scan(requests, initial_position):
    head_movements = 0  #
    current_position = initial_position 

    # split requests into two parts: those below and above the initial position
    below = [r for r in requests if r <= initial_position]
    above = [r for r in requests if r > initial_position]

    # service the requests below the initial position first (in reverse order)
    for request in reversed(below):
        head_movements += abs(request - current_position)  # add distance to the next request
        current_position = request 
    if below:
        head_movements += abs(0 - current_position)  # move to cylinder 0 if there were requests below
        current_position = 0  
        
    # service the requests above the initial position
    for request in above:
        head_movements += abs(request - current_position)  
        current_position = request  

    return head_movements  

# C-SCAN (Circular SCAN) algorithm implementation
def c_scan(requests, initial_position):
    head_movements = 0  
    current_position = initial_position 

    # split requests into two parts: those below and those above the initial position
    below = [r for r in requests if r <= initial_position]
    above = [r for r in requests if r > initial_position]

    # service the requests above the initial position first
    for request in above:
        head_movements += abs(request - current_position) 
        current_position = request  
    if above:
        head_movements += abs(4999 - current_position)  # move to the maximum cylinder (4999) if there were requests above
        current_position = 4999  # set the current position to 4999
    head_movements += abs(4999 - 0)  # wrap around from the maximum cylinder to 0
    current_position = 0 

    # service the requests below the initial position
    for request in below:
        head_movements += abs(request - current_position)  
        current_position = request 

    return head_movements 

def main():
    if len(sys.argv) != 2:
        print("Usage: python disk_scheduler.py <file_name>")
        return

    file_name = sys.argv[1]

    requests = read_requests(file_name)
    # generate a random initial position for the disk head
    initial_position = random.randint(0, 4999)

    print(f"Initial Position: {initial_position}")

    # print results
    print("Original Results:")
    print("FCFS:", fcfs(requests, initial_position))
    print("SCAN:", scan(requests, initial_position))
    print("C-SCAN:", c_scan(requests, initial_position))

    # print optimized results
    print("Optimized Results:")
    optimized_requests = sorted(requests)  # sort the requests to optimize
    print("FCFS:", fcfs(optimized_requests, initial_position))
    print("SCAN:", scan(optimized_requests, initial_position))
    print("C-SCAN:", c_scan(optimized_requests, initial_position))

if __name__ == "__main__":
    main()
