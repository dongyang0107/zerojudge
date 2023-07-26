#一元二次方程式

while True:
	a, b, c = map(int, input().split())
	if b*b-4*a*c >= 0:
		# 在Python中，變數宣告是不需要的，只需要對變數進行賦值即可
		# 會導致出現SyntaxError: invalid syntax錯誤
		# int x1
		# int x2
		x1 = (-b + pow((b*b-4*a*c), 0.5))/2
		x2 = (-b - pow((b*b-4*a*c), 0.5))/2
		# {:.0f}：為了讓得出的結果可以為2, 5，而非2.0, 5.0
		if x1 != x2:
			print('Two different roots x1={:.0f}, x2={:.0f}'.format(x1, x2))
		else:
			print('Two same roots x={:.0f}'.format(x1))
	else:
		print('No real root')