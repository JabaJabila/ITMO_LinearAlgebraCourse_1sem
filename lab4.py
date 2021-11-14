from itertools import permutations, combinations

def dots_of_intersection(plane1, plane2, plane3):
	p1 = plane1[:]
	p2 = plane2[:]
	p3 = plane3[:]
	p1[3] = 0 - p1[3]
	p2[3] = 0 - p2[3]
	p3[3] = 0 - p3[3]
	if not (p1[0] and p2[1]):
		return -1

	c = p2[0] / p1[0]
	for i in range(4):
		p2[i] -= p1[i] * c

	c = p3[0] / p1[0]
	for i in range(4):
		p3[i] -= p1[i] * c

	if p2[1] == 0:
		p2, p3 = p3[:], p2[:]
	if p2[1] == 0:
		 return -1

	c = p3[1] / p2[1]
	for i in range(1, 4):
		p3[i] -= p2[i] * c

	try:
		z = p3[3] / p3[2]
		y = (p2[3] - z * p2[2]) / p2[1]
		x = (p1[3] - z * p1[2] - y * p1[1]) / p1[0]
	except:
		return -1

	return [x + 0, y + 0, z + 0]

def check_point(d, planes):
	for i in planes:
		if (d[0] * i[0] + d[1] * i[1] + d[2] * i[2] + i[3]) > 0:
			return False
	return True

def check_rib(d, planes):
	for i in combinations(planes, 2):
		if (d[0] * i[0][0] + d[1] * i[0][1] + d[2] * i[0][2] + i[0][3] == 0 and 
		d[0] * i[1][0] + d[1] * i[1][1] + d[2] * i[1][2] + i[1][3] == 0):
			return True
	return False

inputf = list(open("input.txt"))

n = int(inputf[0])
planes = []

for i in range(n):
	tmp = inputf[1 + i].split()
	planes.append([float(tmp[0]), float(tmp[1]), float(tmp[2]), 0 - 
		(float(tmp[3]) * float(tmp[0]) + float(tmp[4]) * float(tmp[1]) + float(tmp[5]) * float(tmp[2]))])

dots = []
points = []

for i in permutations(planes, 3):
	point = dots_of_intersection(i[0], i[1], i[2])
	if point != -1 and point not in dots:
		dots.append(point)

for i in dots:
	if check_point(i, planes):
		points.append(i)

ribs = []
for i in combinations(points, 2):
	mid = [(i[0][0] + i[1][0]) / 2, (i[0][1] + i[1][1]) / 2, (i[0][2] + i[1][2]) / 2]
	if check_rib(mid, planes):
		ribs.append(i[0] + i[1])

outputf = open("output.txt", "w")

if len(ribs) >= 6:

	outputf.write(str(len(ribs)) + "\n")
	for i in ribs:
		outputf.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5]) + "\n")
else:
	outputf.write("0\n")

outputf.close()