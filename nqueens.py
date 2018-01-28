#!/usr/bin/python

N = 8

rows         = [0 for i in xrange(N)]
columns      = [False for i in xrange(N)]
diagonals1   = [False for i in xrange(2*N - 1)]
diagonals2   = [False for i in xrange(2*N - 1)]
numSolutions = 0

def printBoard():
	global numSolutions

	numSolutions += 1
	print "==== Solution #{} ====\n".format(numSolutions)

	for queenCol in rows:
		print "".join([" 1" if col == queenCol else " 0" for col in xrange(N)])
	print

def doRow(row):
	d1 = row
	d2 = row + N - 1

	for col in xrange(N):
		if not (columns[col] or diagonals1[d1] or diagonals2[d2]):
			rows[row] = col
			columns[col] = True
			diagonals1[d1] = True
			diagonals2[d2] = True

			if row + 1 == N:
				printBoard()
			else:
				doRow(row + 1)

			columns[col] = False
			diagonals1[d1] = False
			diagonals2[d2] = False
		d1 += 1
		d2 -= 1

if __name__ == "__main__":
	doRow(0)

	print "There are {} solutions.".format(numSolutions)
