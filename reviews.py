# 每讀1000筆，印出數字

import time
tStart = time.time()

time.sleep(2)
data = []
count = 0
with open('reviews.txt', 'r') as f: # as f： 當作 f (file)
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

tEnd = time.time() #計時結束
print("It cost %f sec" % (tEnd - tStart)) #會自動做進位




