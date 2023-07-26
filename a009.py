# 解碼器

# end=‘ ’可以讓輸出不換行
# ord是將字元轉成ascii碼，且ord為int型態，為數字
# chr是將ascii碼轉成字元
word = input()
for i in word:
	print(chr(ord(i)-7), end='')