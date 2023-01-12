# 6. Write lambda functions to find the area of square, rectangle and triangle.

area_square=lambda x: x*x       #area of square is a^2
side=int(input('Enter a side value of square : '))
print(area_square(side))

area_rectangle=lambda x,y:x*y   #area of rectangle is l*w
Length=int(input('Enter a Length value of rectangle : '))
width=int(input('Enter a width value of rectangle : '))
print(area_square(Length))

area_triangle =lambda x,y:(x*y)/2
base=int(input('Enter a base value of triangle : '))
height=int(input('Enter a height value of triangle : '))
print(area_triangle(base,height))