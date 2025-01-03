import sys

words = {}

for line in sys.stdin:
	word, count = line.strip().split()
	count = int(count)
	if word not in words:
		words[word] = count
	else:
		words[word] += count

for word in words:
	print(word+"\t"+str(words[word]))

