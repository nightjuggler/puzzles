#!/usr/bin/python

def base3(n):
	n, r = divmod(n, 3)
	s = str(r)
	while n != 0:
		n, r = divmod(n, 3)
		s = str(r) + s
	return s

def printn(n):
	i = 0
	while n & 1 == 0:
		n >>= 1
		i += 1

	z = "" if i == 0 else "0"*i if i <= 4 else "0*" + str(i)

	print "{0:32b} {2:4} {0:9} {1:>20}".format(n, base3(n), z)

	return n

def collatz(n):
	n = printn(n)
	i = 0

	while n != 1:
		n += (n << 1) + 1
		n = printn(n)
		i += 1

	print "{} steps".format(i)

def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("number")
	parser.add_argument("base", nargs="?", default=0, type=int)
	args = parser.parse_args()

	collatz(int(args.number, base=args.base))

if __name__ == "__main__":
	main()
