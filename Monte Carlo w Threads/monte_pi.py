# imports
import sys
import threading
import random
import math
import time

# global variable
inside_count = 0

# function to calculate number of points inside circle
def monte_carlo(start_index, end_index):

    global inside_count
    
    for i in range(start_index, end_index):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = (x**2 + y**2)**0.5
        if distance <= 1:
            inside_count += 1
        
        
            
# main function
def main():
    
    global inside_count

    # get number of threads and points from command line args
    threads = int(sys.argv[1])
    points = int(sys.argv[2])
    print(f"\nThreads: {threads}\nPoints: {points}")

    # generate random seed based on time
    random.seed(int(time.time()))

    # partition
    partition_size = points // threads
    start_index = 0
    t = [0]*threads
    inside_count = 0

    # intialize timer
    startTime = time.time()

    # initialize threads
    for i in range(0, threads):
        t[i] = threading.Thread(target=monte_carlo, args=(start_index, start_index+partition_size-1))
        t[i].start()
        start_index += partition_size

    # join threads
    for i in range(0, threads):
        t[i].join()
        
    # calculate estimated pi
    ratio = inside_count / points
    estimated_pi = 4 * ratio

    # calculate delta pi
    delta = round(abs(estimated_pi - math.pi), 4)

    # calculate time
    endTime = time.time()
    runTime = round(endTime - startTime, 6)

    # print results
    print("Estimated pi =", estimated_pi)
    print("Delta pi =", delta)
    print("Execution time (sec) =", runTime)



if __name__ == "__main__":
    main()