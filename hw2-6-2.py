# author: CCG 9/23/21

radius = input("What is the radius of the cylinder")
height = input("What is the height of the cylinder")

volume = 3.14 * (int(radius)) ** 2 * int(height)

surface_area = 2 * 3.14 * (int(height) + int(radius))

print(volume)
print(surface_area)
