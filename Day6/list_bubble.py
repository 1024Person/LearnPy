import random
i = 0
random_list=[]
while i<10:
	ran = random.randint(1,20)
	if ran not in random_list:
		random_list.append(ran)
		continue
	i+=1
print(random_list)
swaped = True

l = len(random_list)
for i in range(len(random_list)):
	if swaped:
		swaped = False
		j =0				
		# 刚才一不小心把让 j = 0导致了最后最大的或者最小得数位置不对
		# 而 0-1 = -1所以，刚开始上来比较的就是 第0个 和 第10个
		# 所以这个列表的开头就是从 -1 开始看的了
		while j < l-i:
			if random_list[j] < random_list[j-1]:
				random_list[j],random_list[j-1] = random_list[j-1],random_list[j]
				swaped = True
			j+=1
print(random_list)

def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("排序后的数组:")
print(arr)