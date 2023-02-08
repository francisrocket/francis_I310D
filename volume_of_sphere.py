def compute_volume_of_sphere(radius):
	pi = 3.14
	vol = (4/3) * pi * radius ** 3
	return vol

radius1 = 30
vol1 = compute_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {vol1}")

radius2 = 40
vol2 = compute_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {vol2}")
