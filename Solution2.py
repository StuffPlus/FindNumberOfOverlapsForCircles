import math
import random
import time


start_time = time.time()  # Start timing the code
# generate a random number between 1 and 10000
num_circles = random.randint(1, 10000)  # generate random number of circles

# generate a random number for the x,y and radius
circle = [(random.random(), random.random(), random.random()) for x in range(num_circles)]


# This compares the every circle to each other in order to find overlaps
def count_circle_overlaps(circles):
    count = 0
    for i in range(len(circles)):  # loop through list of circles
        for j in range(i + 1, len(circles)):  # loop through list of circles + 1
            x1, y1, r1 = circles[i]  # load first circle i
            x2, y2, r2 = circles[j]  # load second circle j
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # find the distance between centers
            if distance <= r1 + r2:  # if distance is less than the sum of the radii add 1 to counter as there is an
                # overlap
                count += 1
    return count


print(f' Number of overlaps: {count_circle_overlaps(circle)}')  # print number of overlaps

print("--- %s seconds ---" % (time.time() - start_time))  # print the time taken assuming the code takes at least 0.1
# seconds to run
