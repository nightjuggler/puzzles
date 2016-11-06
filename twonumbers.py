#!/usr/bin/python
import math

minNumber = 2
maxNumber = 100

factorsCache = {}
validSumCache = {}

def factors(N):
	if N in factorsCache:
		return factorsCache[N]

	_factors = [(a, b) for a, (b, c) in [(a, divmod(N, a)) for a in xrange(2, int(math.sqrt(N)) + 1)]
		if c == 0 and minNumber <= a <= maxNumber and minNumber <= b <= maxNumber]

	factorsCache[N] = _factors
	return _factors

def isValidSum(N):
	if N in validSumCache:
		return validSumCache[N]

	for m in xrange(minNumber, maxNumber + 1):
		n = N - m
		if n < minNumber:
			break
		if n > maxNumber:
			continue
		if len(factors(m * n)) == 1:
			validSumCache[N] = False
			return False

	validSumCache[N] = True
	return True

def solve():
	possibleSums = {}

	for m in xrange(minNumber, maxNumber + 1):
		for n in xrange(m, maxNumber + 1):
			#
			# The script runs twice as fast if we first weed out pairs of numbers by the 2nd statement!
			#
			# S replies: "Yeah, I already knew that."
			#
			if not isValidSum(m + n):
				continue
			#
			# P says: "I can't figure out what the two numbers are."
			#
			possible = factors(m * n)
			if len(possible) == 1:
				continue
			#
			# P replies: "Oh, really, well now I know what the two numbers are."
			#
			possible = [(a, b) for a, b in possible if isValidSum(a + b)]
			if len(possible) > 1:
				continue
			#
			# There must be at least one factorization that's also a valid sum: (m, n)
			# In other words, at this point, possible == [(m, n)]
			#
			possibleSums.setdefault(m + n, []).append(possible[0])
	#
	# S replies: "Oh, really, well now I do too."
	#
	for v in possibleSums.itervalues():
		if len(v) == 1:
			print v[0]

if __name__ == '__main__':
	solve()
