def bxor_total(total, i):
	if total[0][i]=='b' or total[0][i]=='.':
		return total[0][i]
	for single in total:
		if single[i]!=total[0][i]:
			return 0
	return 1

def full(bs):
	arr = bs.split('b')
	return "{0}{1}{2}".format('0b','0'*(10-len(bs)),arr[1])

def generate_mask(source):
	total = []
	for item in source:
		array = []
		for single in item.split('.'):
			single = bin(int(single))
			array.append(full(str(single)))

		total.append("{0}.{1}.{2}.{3}".format(array[0],
			array[1],array[2],array[3]))
	print total
	result = []
	for o in range(len(total[0])):
		c = bxor_total(total, o)
		result.append(c)
	four = ''.join(str(i) for i in result).split('.')
	sum =''
	final = []
	for one in four:
		one = "{0}{1}".format('0',one[1:])
		final.append(str(eval(one)))
	print '.'.join(final)


if __name__ == "__main__":
	print "py is a better language over all rubbish like Lua"
	source = ["194.85.160.177", "194.85.160.183", "194.85.160.178"]
	generate_mask(source)
