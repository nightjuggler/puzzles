#!/usr/bin/python

# Is minMoves = 2 * (numCaves - 2) for all numCaves > 2? (True at least for numCaves = 3 thru 7)

numCaves = 5
allCaves = range(numCaves)
maxCave = numCaves - 1
moves = []
prevStates = set()
minMoves = None

def solve(dragonCaves):
	global minMoves
	if minMoves is not None and len(moves) >= minMoves:
		return
	state = tuple(dragonCaves)
	if state in prevStates:
		return
	prevStates.add(state)
	for move in allCaves:
		moves.append(move)
		nextCaves = set()
		for cave in dragonCaves:
			if cave > 0:
				if move != cave - 1:
					nextCaves.add(cave - 1)
			if cave < maxCave:
				if move != cave + 1:
					nextCaves.add(cave + 1)
		if nextCaves:
			solve(nextCaves)
		else:
			if minMoves is None or len(moves) <= minMoves:
				minMoves = len(moves)
				print minMoves, moves
		moves.pop()
	prevStates.remove(state)

if __name__ == '__main__':
	import argparse
	import sys

	parser = argparse.ArgumentParser()
	parser.add_argument('number_of_caves', nargs='?', default=numCaves, type=int)
	args = parser.parse_args()

	if args.number_of_caves < 1:
		sys.exit("The number of caves must be a positive integer.")

	if args.number_of_caves != numCaves:
		numCaves = args.number_of_caves
		allCaves = range(numCaves)
		maxCave = numCaves - 1

	solve(allCaves)
