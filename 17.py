shape = input("Enter a shape: ")

if shape == "sphere":
    radius = float(input("Enter a radius: "))
    volume = 1.33 * 3.14 * radius ** 3

elif shape == "cube":
    length = int(input("Enter the length: "))
    volume = length ** 3

elif shape == "cuboid":
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))
    height = int(input("Enter the height: "))
        volume = length * height * breadth

print("volume of", shape, "is", volume, "cubic units")
