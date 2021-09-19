a = 0

def test():
	a += 1
	return True

if test():
	print("true")

print(a)