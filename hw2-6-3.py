# author: CCG 9/23/21

free_throw = input("how many free throws were made?")
two_points = input("how many two pointers were made?")
three_points = input("how many three pointers were made?")

total_pts = (int(free_throw)) + (int(two_points) * 2) + (int(three_points) * 3)

print(total_pts)
