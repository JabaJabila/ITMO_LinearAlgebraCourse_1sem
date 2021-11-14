import math

def scalar_multi(vector1, vector2):
	return vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

def get_len(vector):
	return (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5

def get_cos(vector1, vector2):
	return (scalar_multi(vector1, vector2) / (get_len(vector1) * get_len(vector2)))

inputf = list(open("input.txt"))

tmp = inputf[0].split()
coords = [float(tmp[0]), float(tmp[1]), 0]
tmp = inputf[1].split()
a = [float(tmp[0]), float(tmp[1]), 0]
tmp = inputf[2].split()
m = [float(tmp[0]), float(tmp[1]), 1]
tmp = inputf[3].split()
en = [float(tmp[0]), float(tmp[1]), 0]

m_angle = math.degrees(math.acos(get_cos(m, [0, 0, 1])))
direction = [en[0] - coords[0], en[1] - coords[1], en[2] - coords[2]]
n = [-a[1], a[0], a[2]]
beta = math.degrees(math.acos(get_cos(n, direction)))
sign = True if math.degrees(math.acos(get_cos(a, direction))) <= 90 else False
bort = 1 if beta <= 90 else -1
bort = 0 if beta > 60 and beta < 120 else bort
beta = beta if beta < 90 else 180 - beta
beta = beta if sign else -beta
m_angle = m_angle if sign else -m_angle

outputf = open("output.txt", "w")

if bort == 0 or m_angle > 60:
	outputf.write("0\n")

else:
	outputf.write(str(bort) + "\n")
	outputf.write(str(beta) + "\n")
	outputf.write(str(m_angle) + "\n")
	outputf.write("bruh...\n")

outputf.close()