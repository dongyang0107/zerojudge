# 因數分解

n = int(input())
d = 2 # 最小因數為2
l = []
while n != 1:
	if n % d == 0:
		n = n / d
		l.append(d)
		# 重置
		d = 2
		continue
	d += 1
x = 0
# 以確保檢查完所有的list
while x < len(l):
	# 因數有重複
	# list count：看列表裡有幾個重複的數
	if l.count(l[x]) > 1:
		print(l[x], "^", l.count(l[x]), sep="", end="")
		# 跳過因數的重複項
		x += l.count(l[x])
	else:
		# 若沒有重複代表只出現一次
		print(l[x], end="")
		x += 1
	# 若不相等代表還有因數沒有輸出，所以用*連接下一個因數
	# 因為當x == len(l)時代表已經檢查完整個列表
	if x != len(l):
		print(" * ", end="")

#########

# n = int(input())
# tmp = []
# #從2跑到無限大(此處設無限大為1e9)
# for i in range(2, int(1e9)):
# 	if n == 1:
# 		# 終止條件
# 		break
# 	# while迴圈執行次數 = 次方數  
# 	cnt = 0
# 	# while not <condition>
# 	# 若<condition>為假(即零、空等，not<condition>的结果為真(True)
# 	# 因此如果n能整除i，代表n%i==0，就進入while迴圈
# 	# n需要在滿足的條件下才可不斷更新
# 	# 而此方式可確保只有n能整除i的情況下再進入迴圈
# 	# while not n % i:
# 	while n % i == 0:
# 		cnt += 1 #次方+1
# 		# n = n//i 
# 		n //= i #更新n(整數除法用 "//")
# 	# if cnt：若cnt的值為非零，代表條件為真，就會繼續執行
# 	# 假如cnt不為0(至少有1次方)，則將[i(必為質因數), cnt(必不為0)]推入tmp
# 	# if cnt != 0:
# 	if cnt: 
# 		tmp.append([i,cnt])

# # 存放要輸出的陣列(不需要存 *，輸出時會加入)
# ans=[]
# # 依序取出tmp所存放的所有[i,cnt]
# for i, cnt in tmp:  
# 	if cnt > 1:
# 		# 次方數大於1，需要另外加上次方數
# 		ans.append(f'{i}^{cnt}')
# 	else:
# 		# 若次方數為1，不需加上次方
# 		ans.append(i)
# # 輸出並加入*在每個ans值的中間
# # *ans相當於ans[0], ans[1], ans[2], ans[3]...：相當於將ans中的元素拆解成獨立的參數 
# # sep=' * '：若為list用於list和list之間做連接
# print(*ans, sep=' * ')