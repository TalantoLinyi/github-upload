

file_name = "3000_words.txt"

with open(file_name, 'r') as f:
	lines = f.read()
	words = lines.split('\n')
	#print(words)
	
words = [word for word in words if len(word)>1]
#print(len(words))

import random
N = 300
random.seed(2)
testwords = random.sample(words, N)
#print(testwords)

# testwords_200 = "\n".join(testwords[:200])
# print(testwords_200)

# with open("200_words", 'w') as f:
# 	f.write(testwords_200)

c = 'a'
for i in range(26):	
	print(chr(ord(c)+i), "")
	
# cnt = 0
# num_r = 0
# for word in testwords:
# 	print("%d/%d  %s" %(cnt+1, N, word))
# 	cnt += 1
# 	s = input("please enter y/n:")
# 	#s = 'z'
# 	while s != 'z' and s!= 'x':
# 		s = input("please enter y/n:")
# 	if s=='z':
# 		num_r += 1

# 	print("current correct rate: %d / %d" %(num_r, cnt))
# 	print()

# rate = num_r/N*100
# print("final correct rate: %.2f%%" %(rate))


