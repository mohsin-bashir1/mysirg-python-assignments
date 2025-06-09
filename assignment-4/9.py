#Write a python script to calculate the volume of a cuboid.

print("Enter the length breadth and height of a cuboid in meters: ")

length, breadth, height = int(input()), int(input()), int(input())

volume = length * breadth * height

print(f"The volume of cuboid with length {length} breadth {breadth} height {height} is {volume} cubic meters.")