#program to calculate the area of the building

#method 1
#program takes the length,breadth and height of the building in metres.
def building_area(l,b,h):
    print("Area of the building is",2*(l*b+h*b+h*l),"metre-square")

building_area(2,3,4)

#output = Area of the building is 52 metre square

#method 2

l = int(input("Enter the length  of the building (in m): "))
b = int(input("Enter the breadth of the building (in m): "))
h = int(input("Enter the hieght  of the building (in m): "))

print("Area of the building is",2*(l*b+b*h+h*l),"metre-square")
