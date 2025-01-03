import sys
chars_to_remove = (".", ",", "!", "?", "'", "\"", ":", ";", "(", ")")

for line in sys.stdin:
	for chars in chars_to_remove:
		line = line.replace(chars, "")
	words = line.lower().strip().split()
	for word in words:
		print(f"{word}\t1")
