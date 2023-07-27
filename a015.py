# 矩陣翻轉

r, c = map(int, input().split())
# 建立r*c的二維矩陣，將所有元素初始化為0
l = [[0]*c] * r
print(l)
for i in range(r):
	l[i] = input().split()
for i in range(c):
	for j in range(r):
		print(l[j][i], end=' ')
	print()

#########
# r,c = map(int, input().split())
# matrix = []
# for i in range(r):
#     matrix.append([int(x) for x in input().split()])
# for i in range(c):
#     for mat in matrix:
#         print(mat[i],end=' ')
#     print()