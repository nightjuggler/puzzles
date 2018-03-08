#!/usr/bin/python

def int2str(n, radix=3):
	n, r = divmod(n, radix)
	s = str(r)
	while n != 0:
		n, r = divmod(n, radix)
		s = str(r) + s
	return s

def printn(n):
	i = 0
	while n & 1 == 0:
		n >>= 1
		i += 1

	z = "" if i == 0 else "0"*i if i <= 4 else "0*" + str(i)

	print "{0:32b} {2:4} {0:9} {1:>20}".format(n, int2str(n), z)

	return n

def collatz(n):
	n = printn(n)
	i = 0

	while n != 1:
		n += (n << 1) + 1
		n = printn(n)
		i += 1

	print "{} steps".format(i)

def printn_binstr(s):
	i = 0
	while s[-(i + 1)] == "0":
		i += 1
	if i > 0:
		s = s[:-i]

	z = "" if i == 0 else "0"*i if i <= 4 else "0*" + str(i)
	n = int(s, base=2)

	print "{:>32} {:4} {:9} {:>20}".format(s, z, n, int2str(n))

	return s

def three_x_plus_one(s):
	r = ""
	j = len(s) - 1

	while j >= 0:
		c = s[j]
		i = j - 1
		while i >= 0 and s[i] == c:
			i -= 1

		d = "0" if c == "1" else "1"
		r = d + s[i+1:j] + d + r
		j = i - 1

	return "1" + r

def collatz_binstr(n):
	s = "{:b}".format(n)
	s = printn_binstr(s)
	i = 0

	while s != "1":
		s = three_x_plus_one(s)
		s = printn_binstr(s)
		i += 1

	print "{} steps".format(i)

def groupify(n):
	groups = []
	lastDigit = None

	for digit in "{:b}".format(n):
		if digit != lastDigit:
			lastDigit = digit
			groups.append(1)
		else:
			groups[-1] += 1

	return groups

def ungroupify(groups):
	return "".join([str(i & 1) * n for i, n in enumerate(groups, 1)])

def printn_groups(groups):
	i = 0
	if len(groups) & 1 == 0:
		i = groups.pop(-1)

	z = "" if i == 0 else "0"*i if i <= 4 else "0*" + str(i)
	s = ungroupify(groups)
	n = int(s, base=2)

	print "{:>32} {:4} {:9} {:>20} {:>30}".format(s, z, n, int2str(n), ",".join(map(str, groups)))

def three_x_plus_one_groups(groups):
	i = len(groups) - 1
	groups.append(0)

	while i >= 0:
		groups[i] -= 1
		groups[i + 1] += 1
		j = i - 1
		if j < 0:
			groups[0:0] = [1, 1]
			i += 2
		elif groups[j] == 1:
			j -= 1
			if j < 0:
				groups[0] += 1
		else:
			groups[j] -= 1
			groups[j+1:j+1] = [0, 1]
			i += 2
		if groups[i] == 0:
			groups[i - 1] += groups[i + 1]
			groups[i:i+2] = []
		i = j

def collatz_groups(n):
	groups = groupify(n)
	printn_groups(groups)
	i = 0

	while len(groups) > 1 or groups[0] > 1:
		three_x_plus_one_groups(groups)
		printn_groups(groups)
		i += 1

	print "{} steps".format(i)

def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("number")
	parser.add_argument("base", nargs="?", default=0, type=int)
	parser.add_argument("-b", "--binary-string", action="store_true")
	parser.add_argument("-g", "--binary-groups", action="store_true")
	args = parser.parse_args()

	n = int(args.number, base=args.base)
	assert n > 0

	if args.binary_groups:
		collatz_groups(n)
	elif args.binary_string:
		collatz_binstr(n)
	else:
		collatz(n)

if __name__ == "__main__":
	main()
