#collect the radius and save it in variable radius
#collect the length and save it in variable length;
#raise the radius to the power of two to get area;
#multiply the  area with the length to get the  volume.


radius = int(input('put in the radius: '))

length = int(input('put in the length: '))

PI=3.142

area =PI * radius**2
 
volume = area * length


print(f"{volume}")
