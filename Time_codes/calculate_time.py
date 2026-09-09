import time

# start time
start = time.time()

# loop to measure
for i in range(1000000):
    x = i * 2   # some operation

# end time
end = time.time()

# total time taken
print("Loop execution time:", end - start, "seconds")
