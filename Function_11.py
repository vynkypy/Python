import time
import numpy as np

# First loop
start1 = time.time()
ls = []
for i in range(1, 700000000):
    ls.append(i)

end1 = time.time()
print("Time for first loop:", end1 - start1, "seconds")


# Second = loop
start2 = time.time()

arr = np.arange(1, 700000000)

end2 = time.time()
print("Time for second loop:", end2 - start2, "seconds")
