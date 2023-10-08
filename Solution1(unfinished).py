import math
import random
import time


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_circle_dimensions(self):
        return self.x, self.y, self.r


class Overlap:
    def __init__(self):
        self.circle_count = None
        self.list_of_circles = []

    def insert_circle(self, circle):
        self.list_of_circles.append(circle)

    def generate_circles(self, circle_count):
        self.circle_count = circle_count  # store circles

        # generate a random number for the (x,y) coordinates and the radius
        for x in range(self.circle_count):
            circle = Circle(random.randint(0, 2000), random.randint(0, 2000), random.randint(1, 10))
            self.insert_circle(circle)  # store in a list

    # This compares the every circle to each other in order to find overlaps
    # Does not check itself as it always starts from +1 from the initial circle
    def count_circle_overlaps(self):
        count = 0
        for i in range(len(self.list_of_circles)):  # loop through list of circles
            for j in range(i + 1, len(self.list_of_circles)):  # loop through list of circles + 1
                x1, y1, r1 = self.list_of_circles[i].get_circle_dimensions()  # load first circle i
                x2, y2, r2 = self.list_of_circles[j].get_circle_dimensions()  # load second circle j
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # find the distance between centers
                if distance <= r1 + r2:  # if distance is less than the sum of the radii add 1 to counter as there is an
                    # overlap
                    count += 1
        return count


def main(count):
    overlap = Overlap()  # initialise the class Overlap
    overlap.generate_circles(count)  # number of circles to be randomly generated
    print(f'Number of circles: {len(overlap.list_of_circles)}')
    start_time = time.perf_counter()  # Start timing the code
    print(f'Number of overlaps: {overlap.count_circle_overlaps()} ')
    end = time.perf_counter()  # get end time of code
    time_taken = end - start_time  # find the difference
    print(f'Time taken in seconds: {time_taken:.4}s\n')  # seconds to run


main(1000)
main(1000)
main(1000)

main(2000)
main(2000)
main(2000)

main(5000)
main(5000)
main(5000)

main(10000)
main(10000)
main(10000)

main(15000)
main(15000)
main(15000)

main(20000)
main(20000)
main(20000)