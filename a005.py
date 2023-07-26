# 等差等比數列

n = int(input())
# 初始化矩陣
# a = []
for i in range(n):
	# 若沒有用int(x)則用戶輸入的每個數字將被視為字串而非整數，
	# 這將導致a列表中存儲的是字串而不是數字
	# 將這個整數列表存儲在變數a中
	a = [int(x) for x in input().split()]
	# a.append([int(x) for x in input().split()])
	# 公差
	if(a[3]-a[2] == a[2]-a[1] == a[1]-a[0]):
		d = a[2]-a[1]
		a.append(a[3]+d)
	else:
		r = a[2]//a[1]
		a.append(a[3]*r)
	# 可以將列表中的元素單獨打印出來
	# 不會包含列表的方括號和逗號，並使用預設的空格作為分隔符
	print(*a)

##########

# n = int(input())
# for i in range(n):
# 	a, b, c, d = map(int, input().split())
# 	# 等差
# 	if(b-a == c-b == d-c):
# 		print(a, b, c, d, d+(d-c))
# 	# 等比
# 	else:
# 		# 等比數列的比值也是自然數：d//c
# 		print(a, b, c, d, d*d//c)