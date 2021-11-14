def sum_matrix(A, B):

	n = len(A)
	m = len(A[0])
	C = []
	for i in range(n):
		C.append([])
		for j in range(m):
			C[i].append(A[i][j] + B[i][j])
	return C

def multiply_const(x, A):

	n = len(A)
	m = len(A[0])
	for i in range(n):
		for j in range(m):
			A[i][j] *= x
	return A

def multiply_matrix(A, B):

	n1 = len(A)
	m1 = len(A[0])
	n2 = len(B)
	m2 = len(B[0])
	if (m1 != n2):
		return "Unable to multiply"
	C = []
	for i in range(n1):
		C.append([])
		for j in range(m2):
			C[i].append(0)
			for k in range(m1):
				C[i][j] += A[i][k] * B[k][j]
	return C

def trans_matrix(A):
	n = len(A)
	m = len(A[0])
	C = []
	for i in range(m):
		C.append([])
		for j in range(n):
			C[i].append(A[j][i])
	return C

def lab1_task(A, B, C, D, F, a, b):
	try:
		return sum_matrix(multiply_matrix(multiply_matrix(C, 
			trans_matrix(sum_matrix(multiply_const(a, A), 
			multiply_const(b, trans_matrix(B))))), D), multiply_const(-1, F))
	except:
		return 0

def get_matrix(inputf, ind, n, m):
	A = []
	tmp = inputf[ind].split()
	for i in range(n):
		A.append([])
		for j in range(m):
			A[i].append(float(tmp[i * m + j]))
	return A

inputf = list(open("input.txt"))

tmp = inputf[0].split()
a, b = float(tmp[0]), float(tmp[1])
tmp = inputf[1].split()
n, m = int(tmp[0]), int(tmp[1])
A = get_matrix(inputf, 2, n, m)
tmp = inputf[3].split()
n, m = int(tmp[0]), int(tmp[1])
B = get_matrix(inputf, 4, n, m)
tmp = inputf[5].split()
n, m = int(tmp[0]), int(tmp[1])
C = get_matrix(inputf, 6, n, m)
tmp = inputf[7].split()
n, m = int(tmp[0]), int(tmp[1])
D = get_matrix(inputf, 8, n, m)
tmp = inputf[9].split()
n, m = int(tmp[0]), int(tmp[1])
F = get_matrix(inputf, 10, n, m)

res = lab1_task(A, B, C, D, F, a, b)

outputf = open("output.txt", "w")
if res == 0:
	outputf.write(str(res))
else:
	outputf.write("1\n" + str(len(res)) + " " + str(len(res[0])) + "\n")
	for i in range(len(res)):
		for j in range(len(res[0])):
			outputf.write(str(res[i][j]) + " ")
		outputf.write("\n")

outputf.close()