
from mpi4py import MPI
import math
import random
import time

# number of points to generate
POINTS = 1000000

# MPI init
world = MPI.COMM_WORLD
numprocs = world.size
myid = world.rank

# partitions
s = POINTS // numprocs
s0 = s + POINTS % numprocs

startIndex = s0 + (myid - 1) * s
endIndex = startIndex + s

# generate random seed based on time
random.seed(int(time.time()))

# time start
if myid == 0:
    startwtime = MPI.Wtime()

inside_count = 0

if myid == 0:  # master worker
    for i in range(0, s0):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = (x**2 + y**2)**0.5
        if distance <= 1:
            inside_count += 1
else:  # slave worker
    for j in range(startIndex, endIndex):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = (x**2 + y**2)**0.5
        if distance <= 1:
            inside_count += 1

sum = world.reduce(inside_count, op=MPI.SUM, root=0)
if myid == 0:
    # calculate estimated pi
    ratio = sum / POINTS
    estimated_pi = 4 * ratio

    # calculate delta pi
    delta = round(abs(estimated_pi - math.pi), 4)

    # calculate time
    endwtime = MPI.Wtime()
    runTime = round(endwtime - startwtime, 6)

    # print results
    print("Estimated pi =", estimated_pi)
    print("Delta pi =", delta)
    print("Execution time (sec) =", runTime)

