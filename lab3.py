def scalar_multi(vector1, vector2):
	return vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

def vector_multi(vector1, vector2):
	a = vector1[1] * vector2[2] - vector1[2] * vector2[1]
	b = vector1[0] * vector2[2] - vector1[2] * vector2[0]
	c = vector1[0] * vector2[1] - vector1[1] * vector2[0]
	return [a, 0 - b, c]

def build_plane_eq(A, B, C):
	n = vector_multi([B[0] - A[0], B[1] - A[1], B[2] - A[2]], [C[0] - A[0], C[1] - A[1], C[2] - A[2]])
	D = 0 - (B[0] * n[0] + B[1] * n[1] + B[2] * n[2])
	n.append(D)
	return n

def vector_reflected(l, n):
	tmp = scalar_multi(l, n) / scalar_multi(n, n)
	r1 = l[0] - 2 * n[0] * tmp
	r2 = l[1] - 2 * n[1] * tmp
	r3 = l[2] - 2 * n[2] * tmp
	return [r1, r2, r3]

def find_intersection(point, vector, plane):
	l = plane[0] * vector[0] + plane[1] * vector[1] + plane[2] * vector[2]
	r = plane[0] * point[0] + plane[1] * point[1] + plane[2] * point[2] + plane[3]
	if l == 0:
		return -1
	return (0 - r)/l

class Cube():
	def __init__(self, A, B, C, D):
		self.A = A
		self.B = B
		self.C = C
		self.C1 = D
		self.D = [self.A[0] + self.C[0] - self.B[0], self.A[1] + self.C[1] - self.B[1], self.A[2] + self.C[2] - self.B[2]]
		self.B1 = [self.B[0] + self.C1[0] - self.C[0], self.B[1] + self.C1[1] - self.C[1], self.B[2] + self.C1[2] - self.C[2]]
		self.A1 = [self.A[0] + self.C1[0] - self.C[0], self.A[1] + self.C1[1] - self.C[1], self.A[2] + self.C1[2] - self.C[2]]
		self.D1 = [self.D[0] + self.C1[0] - self.C[0], self.D[1] + self.C1[1] - self.C[1], self.D[2] + self.C1[2] - self.C[2]]
		self.ABCD = build_plane_eq(self.A, self.B, self.C)
		self.AA1BB1 = build_plane_eq(self.A, self.A1, self.B)
		self.AA1DD1 = build_plane_eq(self.A, self.A1, self.D)
		self.DD1CC1 = build_plane_eq(self.D, self.D1, self.C)
		self.BB1CC1 = build_plane_eq(self.B, self.B1, self.C)
		self.A1B1C1D1 = build_plane_eq(self.A1, self.B1, self.C1)

class Mirror():
	def __init__(self, P, Q, R):
		self.P = P
		self.Q = Q
		self.R = R
		self.n = vector_multi([Q[0] - P[0], Q[1] - P[1], Q[2] - P[2]], [R[0] - P[0], R[1] - P[1], R[2] - P[2]])
		self.eq = build_plane_eq(P, Q, R)
		self.intersection = -1 



inputf = list(open("input.txt"))

tmp = inputf[0].split()
A = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
tmp = inputf[1].split()
B = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
tmp = inputf[2].split()
C = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
tmp = inputf[3].split()
D = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
tmp = inputf[4].split()
ray = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
tmp = inputf[5].split()
point = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
energy = int(inputf[6])
n = int(inputf[7])

mirrors = []
for i in range(n):
	tmp = inputf[8 + 3 * i].split()
	P = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
	tmp = inputf[8 + 3 * i + 1].split()
	Q = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
	tmp = inputf[8 + 3 * i + 2].split()
	R = [float(tmp[0]), float(tmp[1]), float(tmp[2])]
	mirrors.append(Mirror(P, Q, R))

cube = Cube(A, B, C, D)

while True:

	closer = 999999
	curr_m = -1
	isInside = True

	for i in range(n):
		x = find_intersection(point, ray, mirrors[i].eq)

		if x > 0 and x < closer:
			closer = x
			curr_m = i

	x = find_intersection(point, ray, cube.ABCD)
	if x > 0 and x < closer:
		closer = x
		isInside = False
	x = find_intersection(point, ray, cube.AA1BB1)
	if x > 0 and x < closer:
		closer = x
		isInside = False
	x = find_intersection(point, ray, cube.AA1DD1)
	if x > 0 and x < closer:
		closer = x
		isInside = False
	x = find_intersection(point, ray, cube.DD1CC1)
	if x > 0 and x < closer:
		closer = x
		isInside = False
	x = find_intersection(point, ray, cube.BB1CC1)
	if x > 0 and x < closer:
		closer = x
		isInside = False
	x = find_intersection(point, ray, cube.A1B1C1D1)
	if x > 0 and x < closer:
		closer = x
		isInside = False

	if not isInside:
		break

	point = [point[0] + closer * ray[0], point[1] + closer * ray[1], point[2] + closer * ray[2]]
	ray = vector_reflected(ray, mirrors[curr_m].n)
	energy -= 1

	print(point, ray)

	if energy == 0:
		break

outputf = open("output.txt", "w")

if not isInside:
	
	outputf.write(str(1) + "\n")
	outputf.write(str(energy) + "\n")
	outputf.write(str(point[0] + closer * ray[0]) + " " + str(point[1] + closer * ray[1]) + " " + str(point[2] + closer * ray[2]) + "\n")
	outputf.write(str(ray[0]) + " " + str(ray[1]) + " " + str(ray[2]) + "\n")

else:
	outputf.write(str(0) + "\n")
	outputf.write(str(point[0]) + " " + str(point[1]) + " " + str(point[2]) + "\n")

outputf.close()